import gdb

class CheckFmtBreakpoint(gdb.Breakpoint):


	def __init__(self, spec):
		super(CheckFmtBreakpoint, self).__init__(
			spec, gdb.BP_BREAKPOINT, internal=False
		)
		gdb.events.exited.connect(lambda x : gdb.execute("quit"))
		gdb.execute('r AA')

	def stop(self):

		gdb.execute('set logging on')		
		for i in range(0,10):
			gdb.execute('x/s *((char **)environ+%d)'%i)
		gdb.execute('set logging off')		

		proc_map = [];
		with open("/proc/%d/maps" % gdb.selected_inferior().pid) as fp:
			f = open( 'procMap.txt', 'w' )
			f.write(fp.read())
	

CheckFmtBreakpoint("main")
'''
CheckFmtBreakpoint("fprintf", 1)
CheckFmtBreakpoint("sprintf", 1)
CheckFmtBreakpoint("snprintf", 2)
CheckFmtBreakpoint("vprintf", 0)
CheckFmtBreakpoint("vfprintf", 1)
CheckFmtBreakpoint("vsprintf", 1)
CheckFmtBreakpoint("vsnprintf", 2)
'''
