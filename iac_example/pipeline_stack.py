from aws_cdk import  core
from aws_cdk import  aws_codepipeline as codepipeline
from aws_cdk import  aws_codepipeline_actions as cpactions
from aws_cdk import  pipelines

class PipelineStack(core.Stack):
    def __init__(self,scope: core.Construct, id:str, **kwargs):
        super().__init__(scope, id ,**kwargs )
        
        source_artifact=codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()
        
        
        pipelines.CdkPipeline(self,'Pipeline',
        cloud_assembly_artifact = cloud_assembly_artifact,
        pipeline_name='pipeline-iac-example',
        source_action=cpactions.GitHubSourceAction(
            action_name='codeCommit',
            output=source_artifact,
            oauth_token=core.SecretValue.secrets_manager('github-token'),
            owner='carolinagzr',
            repo='app1',
            trigger=cpactions.GitHubTrigger.POLL),
             synth_action=pipelines.SimpleSynthAction(
                 source_artifact=source_artifact,
                 cloud_assembly_artifact=classmethod,
                 install_command='yum -y install python3.7 && pip-3.7 install -r requirements.txt',
                 synth_command='cdk synth'))
        