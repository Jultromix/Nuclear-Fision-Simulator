import cx_Freeze

executables = [cx_Freeze.Executable("Fision_motion_Lstv.py")]

cx_Freeze.setup(
    name="Try it",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["Uranio.png","Kripton.png","Bario.png","neutron.png","D.png","He.png","Mg.png","Na.png","T.png","Reactor_bk.png","react1.png","react2.png","react3.png","react4.png","settings.png","Instructions.png"]}},
    executables = executables

    )