use clap::{Parser, Subcommand};
use sysinfo::{Pid, ProcessStatus, Signal, System};
#[derive(Parser)]
#[command(
    name = "cryo",
    about = "Cryo: Process Freezer. Stop apps without closing them.",
    after_help = "Example: cryo freeze firefox"
)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Freeze a process tree
    Freeze {
        /// Process name (e.g., firefox)
        name: String,
    },
    /// Unfreeze a process tree
    Unfreeze {
        /// Process name (e.g., firefox)
        name: String,
    },
    /// Show process status (e.g freeze/running)
    Status {
        /// Process name (e.g., firefox)
        name: String,
    },
    Show,
}

fn is_safe(pid: Pid) -> bool {
    let current_pid = sysinfo::get_current_pid().unwrap_or(Pid::from(0));
    if pid.as_u32() < 1000 || pid == current_pid {
        return false;
    }
    true
}

fn show_all_procs(sys: &System) {
    println!("~~~ Active processes ~~~");
    for (pid, process) in sys.processes() {
        if pid.as_u32() >= 1000 {
            println!("{} - {}", pid.as_u32(), process.name().to_string_lossy());
        }
    }
}

fn proc_status(sys: &System, name: &str) {
    if let Some((_, process)) = sys.processes().iter().find(|(_, p)| p.name().to_string_lossy() == name) {
        if process.status() == ProcessStatus::Stop {
            println!("Process is frozen ❄️");
        } else {
            println!("Process is running 🟢");
        }
    } else {
        println!("Cannot find process {}", name);
    }
}

fn find_pid(sys: &System, name: &str) -> Option<Pid> {
    sys.processes()
        .iter()
        .find(|(_, process)| process.name().to_string_lossy() == name)
        .map(|(pid, _)| *pid)
}

fn find_all_children(sys: &System, parent_pid: Pid, descendant_pids: &mut Vec<Pid>) {
    for (pid, process) in sys.processes() {
        if let Some(ppid) = process.parent() {
            if ppid == parent_pid {
                descendant_pids.push(*pid);
                find_all_children(sys, *pid, descendant_pids);
            }
        }
    }
}

fn main() {
    let cli = Cli::parse();

    let mut sys = System::new_all();
    sys.refresh_all();

    let is_freeze = matches!(cli.command, Commands::Freeze { .. });

    match cli.command {
        Commands::Show => {
            show_all_procs(&sys);
            return;
        }
        Commands::Status { name } => {
            proc_status(&sys, &name);
            return;
        }
        Commands::Freeze { name } | Commands::Unfreeze { name } => {
            let root_pid = match find_pid(&sys, &name) {
                Some(pid) => pid,
                None => {
                    println!("Cannot find process {}", name);
                    return;
                }
            };

            let mut procs_to_manage = vec![root_pid];
            find_all_children(&sys, root_pid, &mut procs_to_manage);

            for pid in procs_to_manage {
                if !is_safe(pid) {
                    println!("System critical process [{}]!!! Skipping.", pid.as_u32());
                    continue;
                }

                if let Some(process) = sys.process(pid) {
                    if is_freeze {
                        if process.kill_with(Signal::Stop).is_some() {
                            println!("Suspended process [{}]", pid.as_u32());
                        } else {
                            println!("Failed to suspend process [{}]", pid.as_u32());
                        }
                    } else {
                        if process.kill_with(Signal::Continue).is_some() {
                            println!("Resumed process [{}]", pid.as_u32());
                        } else {
                            println!("Failed to resume process [{}]", pid.as_u32());
                        }
                    }
                }
            }
            println!("Completed successfully!");
        }
    }
}