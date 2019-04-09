from SpiffWorkflow import Workflow

from architecture.scheduler.spiff_wf_demo import NuclearStrikeWorkflowSpec

spec = NuclearStrikeWorkflowSpec()

wf = Workflow(spec)

wf.complete_all()