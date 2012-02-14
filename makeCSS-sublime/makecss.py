import sublime, sublime_plugin
import subprocess

# Thanks to http://pastie.org/private/bclbdgxzbkb1gs2jfqzehg
class makecssCommand(sublime_plugin.TextCommand):
	def run(self, edit, args):
		if self.view.sel()[0].empty():
			# nothing selected: process the entire file
			region = sublime.Region(0L, self.view.size())
		else:
			# process only selected region
			region = self.view.line(self.view.sel()[0])

		p = subprocess.Popen(
			args,
			shell   = True,
			bufsize = -1,
			stdout  = subprocess.PIPE,
			stderr  = subprocess.PIPE,
			stdin   = subprocess.PIPE)

		output, error = p.communicate(self.view.substr(region).encode('utf-8'))

		if error:
			print "Error: "  + error
		else:
			self.view.replace(edit, region, output.decode('utf-8'))
				
