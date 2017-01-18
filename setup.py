import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="evasion",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["car.png","reds.png"]}},
    executables = executables

    )
