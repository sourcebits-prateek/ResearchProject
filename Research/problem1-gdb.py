import gdb

class CheckFmtBreakpoint(gdb.Breakpoint):


	def __init__(self, spec, fmt_idx):
		super(CheckFmtBreakpoint, self).__init__(
			spec, gdb.BP_BREAKPOINT, internal=False
		)
		gdb.events.exited.connect(lambda x : gdb.execute("quit"))
		gdb.execute('r AA')


	def stop(self):

		proc_map = []
		with open("/proc/%d/maps" % gdb.selected_inferior().pid) as fp:
			proc_map = self._parse_map(fp.read())

		f = open( 'procMap.txt', 'w' )
		for item in proc_map:
			f.write("%s\n" % item)
		
	def _parse_map(self, file_contents):

		zones = []
		for line in file_contents.split('\n'):
			if not line:
				continue
			memrange, perms, _ = line.split(None, 2)
			start, end = memrange.split('-')
			zones.append({
				'start': int(start, 16),
				'end': int(end, 16),
				'perms': perms
			})
		return zones

CheckFmtBreakpoint("printf", 0)
CheckFmtBreakpoint("fprintf", 1)
CheckFmtBreakpoint("sprintf", 1)
CheckFmtBreakpoint("snprintf", 2)
CheckFmtBreakpoint("vprintf", 0)
CheckFmtBreakpoint("vfprintf", 1)
CheckFmtBreakpoint("vsprintf", 1)
CheckFmtBreakpoint("vsnprintf", 2)
