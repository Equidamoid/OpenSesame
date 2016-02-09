#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame.py3compat import *
from libopensesame.keyboard_response import keyboard_response as \
	keyboard_response_runtime
from libqtopensesame.validators import timeout_validator
from libqtopensesame.items.qtplugin import qtplugin
from openexp.keyboard import keyboard
from qtpy import QtCore, QtWidgets
from libqtopensesame.misc.translate import translation_context
_ = translation_context(u'keyboard_response', category=u'item')

class keyboard_response(keyboard_response_runtime, qtplugin):

	"""keyboard_response item GUI"""

	description = _(u'Collects keyboard responses')

	def __init__(self, name, experiment, string=None):

		"""
		Constructor

		Arguments:
		name -- item name
		experiment -- experiment instance

		Keywords arguments:
		string -- a definition string (default=None)
		"""

		keyboard_response_runtime.__init__(self, name, experiment, string)
		qtplugin.__init__(self)

	def init_edit_widget(self):

		"""Initialize controls"""

		super(keyboard_response, self).init_edit_widget(stretch=True)
		# Use auto-controls for most stuff
		self.add_line_edit_control(u'correct_response', _(u'Correct response'),
			tooltip=_(u'Set the correct response'))
		self.add_line_edit_control(u'allowed_responses', _(u'Allowed responses'),
			tooltip=_(u'Set the allowed responses seperated by a semi-colon, e.g., "z;/"'))
		self.add_line_edit_control(u'timeout', _(u'Timeout'),
			tooltip=_(u'Set the response timeout in milliseconds, or "infinite"'),
			validator=timeout_validator(self))
		self.add_checkbox_control(u'flush', _(u'Flush pending keypresses'),
			tooltip=_(u'Flush pending keypresses'))
		# List available keys
		button_list_keys = QtWidgets.QPushButton(
			self.theme.qicon(u"help-about"), _(u"List available keys"))
		button_list_keys.setIconSize(QtCore.QSize(16,16))
		button_list_keys.clicked.connect(self.list_keys)
		self.add_control(u'', button_list_keys, _(u'List available keys'))

	def list_keys(self):

		"""Show a dialog with available key names"""

		my_keyboard = keyboard(self.experiment)
		s = _(u'The following key names are valid:<br />') \
			+ u'<br />'.join(my_keyboard.valid_keys())
		self.experiment.notify(s)
