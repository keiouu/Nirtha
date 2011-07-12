/*
 * jQuery Grid Widget
 *
 * Copyright 2011, James Thompson
 * Dual licensed under the MIT or GPL Version 2 licenses.
 * http://jquery.org/license
 *
 * Depends:
 *	jquery.ui.core.js
 *	jquery.ui.widget.js
 */
(function($) {
	$.widget( "ui.grid", {
		_create: function() {
			var self = this;
			
			// Style
			self.element.addClass("ui-grid");
			self.element.children("p").addClass("row");
			self.element.children("p:even").addClass("row-a");
			self.element.children("p:odd").addClass("row-b");
			
			// Events
			self.element.children("p").mouseover(function(){
				$(this).addClass("row-hover");
			});
			
			self.element.children("p").mouseout(function(){
				$(this).removeClass("row-hover");
			});
		},
	});
})(jQuery);
