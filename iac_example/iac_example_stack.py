from aws_cdk import  core
    # aws_sqs as sqs,


from os import path
import aws_cdk.aws_lambda as lmb
import aws_cdk.aws_apigateway as apigw

from constructs import Construct

class IacExampleStack(core.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        this_dir = path.dirname(__file__)
        
        handler = lmb.Function(self, 'Handler',
            runtime=lmb.Runtime.PYTHON_3_6,
            handler='handler.handler',
            code=lmb.Code.from_asset(path.join(this_dir,'lambda')))
            
        gw=apigw.LambdaRestApi(self,'gateway',
            description='endpoint for a simple Lambda-poweres websesrvice', handler=handler.current_version)

        self.url_output = core.CfnOutput( self,'Url', value=gw.url)        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "IacExampleQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
