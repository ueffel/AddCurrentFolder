import sublime
import sublime_plugin
import os

class AddCurrentFolderCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		dir_name = self.get_current_dir()
		self.add_folder_to_project(dir_name)

	def get_current_dir(self):
		view = self.view
		dir_name = None
		try:
			dir_name = os.path.dirname(view.file_name())
		except:
			pass
		return dir_name

	def add_folder_to_project(self, dir_name):
		folder = {
			'follow_symlinks': True,
			'path': dir_name,
			# 'folder_exclude_patterns': ['.*']
		}
		project_data = sublime.active_window().project_data();
		try:
			folders = project_data['folders']
			for f in folders:
				if f['path'] == dir_name:
					return
			folders.append(folder)
		except:
			folders = [folder]
			if project_data is None:
				project_data = {}
			project_data['folders'] = folders
		sublime.active_window().set_project_data(project_data)
