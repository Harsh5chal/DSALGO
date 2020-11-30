import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Pathfinding Visualizer",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["main_backgroun.png"],
                            "include_files":["grid_logo.png"]}},
    executables = executables

    )