from src.base import SourceLocation, Target

SourceLocation(
	name = 'riscv-gnu-toolchain',
	vcs = 'git',
	location = 'https://github.com/riscv-collab/riscv-gnu-toolchain',
	revision = 'origin/master'
)

Target(
	name = 'riscv-gnu-toolchain',
	sources = [ 'riscv-gnu-toolchain' ],
	license_file = 'riscv-gnu-toolchain/LICENSE',
	package = 'riscv-gnu-toolchain',
)
