/*
 * jQuery Content Holder Widget
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
	$.widget( "ui.content", {
		_create: function() {
			var self = this;
			this.element.addClass("ui-widget ui-widget-content ui-content");
			title = $("<div></div>").text(self.element.attr("title")).addClass("ui-widget-header ui-content-title");
			self.element.prepend(title);
			
			title.next().addClass("ui-content-data");
		},
	});
})(jQuery);
