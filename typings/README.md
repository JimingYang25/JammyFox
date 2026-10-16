# MuJoCo editor types

MuJoCo 3.15.0 exposes simulation functions and enums through compiled extensions
without type stubs. Pylance cannot discover the names re-exported from those
extensions, so it reports valid calls such as `mujoco.mj_step` as unknown
attributes.

`pyrightconfig.json` points to this directory. `mujoco/__init__.pyi` declares the
simulation functions and camera enum used by this project and re-exports the
installed package's structure types and renderer. Submodules such as
`mujoco.viewer` continue to resolve from the installed package. The signatures
match MuJoCo 3.15.0's runtime docstrings. These files are used only by type
checkers and do not affect Python imports.

When adding another top-level MuJoCo API, extend `mujoco/__init__.pyi` with its
runtime signature. Recheck these declarations when upgrading `requirements.txt`.
If VS Code retains old diagnostics after a change, run **Python: Restart Language
Server** from the Command Palette.
