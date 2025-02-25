// Copyright (c) 2025, elifvish and contributors
// For license information, please see license.txt

frappe.ui.form.on("RQ Job Customizer", "create_customizations", function(frm) { 
    frappe.call({
        method: "frappe_rq_job_override.frappe_rq_job_override.doctype.rq_job_customizer.rq_job_customizer.create_customizations",
        callback: function(r) {
            if(r.message) {
                frappe.msgprint(r.message);
            }
        }
    });
});