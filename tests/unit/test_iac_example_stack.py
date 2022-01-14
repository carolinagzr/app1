import aws_cdk as core
import aws_cdk.assertions as assertions

from iac_example.iac_example_stack import IacExampleStack

# example tests. To run these tests, uncomment this file along with the example
# resource in iac_example/iac_example_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = IacExampleStack(app, "iac-example")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
