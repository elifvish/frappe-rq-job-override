# Copyright (c) 2025, elifvish and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from frappe.core.doctype.rq_job.rq_job import  ( 
	RQJob, 
	QUEUES,
	)

from frappe.utils.background_jobs import get_queues

class RQJobCustomizer(Document):
	pass

class RQjobOverride(RQJob):
	custom_queues = frappe.get_site_config().get("workers")
	if custom_queues is not None:
		QUEUES.extend(list(custom_queues.keys()))
	

@frappe.whitelist()
def create_customizations():
	try:
		custom_queues = frappe.get_site_config().get("workers")
		update_options = ("\n").join(QUEUES)

		frappe.get_doc({
			"doctype": "Property Setter",
			"doctype_or_field": "DocField",
			"doc_type": "RQ Job",
			"field_name": "queue",
			"property": "options",
			"value": update_options
		}).insert(ignore_permissions=True)

		update_queue_list = frappe.get_doc("RQ Job Customizer", "RQ Job Customizer")
		update_queue_list.custom_queues = custom_queues
		update_queue_list.save(ignore_permissions=True)

		return "Customization created successfully"
	
	except Exception as e:
		return e
	



