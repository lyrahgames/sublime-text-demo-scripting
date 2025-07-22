import sublime
import sublime_plugin
import os

def send(domain, msg):
  addr = domain + '.fdm'
  tmp = addr + '.send'
  with open(tmp,'w', encoding='utf-8') as file:
    file.write(msg);
  os.rename(tmp, addr)

class demo_scripting_select_all_command(sublime_plugin.TextCommand):
  def run(self, edit):
    domain = self.view.file_name()
    if not domain:
      return
    selection = self.view.substr(sublime.Region(0, self.view.size()))
    send(domain, selection)

class demo_scripting_smart_select_command(sublime_plugin.TextCommand):
  def run(self, edit):
    domain = self.view.file_name()
    if not domain:
      return
    selection = ""
    for region in self.view.sel():
      if region.empty():
        selection += self.view.substr(self.view.line(region)) + '\n'
      else:
        selection += self.view.substr(region) + '\n'
    send(domain, selection)
