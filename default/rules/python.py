from src.base import SourceLocation, Target

SourceLocation(
	name = 'python3',
	vcs = 'git',
	location = 'https://github.com/python/cpython',
	revision = 'tags/v3.8.12'
)

Target(
	name = 'python3',
	sources = [ 'python3' ],
	patches = [ 'python38.diff', 'python38-mingw.diff', 'python38-darwin.diff' ],
	license_file = 'python3/LICENSE',
)

SourceLocation(
	name = 'python2',
	vcs = 'git',
	location = 'https://github.com/python/cpython',
	revision = 'tags/v2.7.18',
)

Target(
	name = 'python2',
	sources = [ 'python2' ],
	patches = [ 'python27.diff', 'python27-darwin.diff' ],
	license_file = 'python2/LICENSE',
)
