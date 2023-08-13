# import required libraries
import os
import boto3
import wavio as wv
import sounddevice as sd
from twilio.rest import Client
from scipy.io.wavfile import write
from botocore.exceptions import NoCredentialsError

class distress:

    @classmethod
    def record(cls): # Recording Audio if there is distress call
        # Sampling frequency
        freq = 44100
        # Recording duration in seconds
        duration = 30
        # Start recorder with the given values
        # of duration and sample frequency
        recording = sd.rec(int(duration * freq),
                        samplerate=freq, channels=2) 
        # Record audio for the given number of seconds
        sd.wait()
        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        write("textbase/distress_audio/recording0.wav", freq, recording)
        # Convert the NumPy array to audio file
        wv.write("textbase/distress_audio/recording.wav", recording, freq, sampwidth=2)

    @classmethod
    def generate(cls): #genrating the link of the audio file to share to towillie
        iam_user_access_key_id = None
        iam_user_secret_access_key = None
        bucket_name = None
        object = None
        # Initialize the STS client using the IAM user's credentials
        sts = boto3.client('sts', aws_access_key_id=iam_user_access_key_id, aws_secret_access_key=iam_user_secret_access_key)

        # Replace 'ASSUMED_ROLE_ARN' with the ARN of the role with necessary permissions
        assumed_role_arn = "arn:aws:iam::630002100053:user/distress-call-record"

        try:
            # Assume the role
            assumed_role = sts.assume_role(
                RoleArn=assumed_role_arn,
                RoleSessionName='AssumedRoleSession'
            )
            
            credentials=assumed_role['Credentials']

            # Use the temporary credentials that AssumeRole returns to make a 
            # connection to Amazon S3  
            s3=boto3.resource(
                's3',
                aws_access_key_id=credentials['AccessKeyId'],
                aws_secret_access_key=credentials['SecretAccessKey'],
                aws_session_token=credentials['SessionToken'],
            )

            # Now you can use the 's3' client to upload the file to S3
            # Replace 'YOUR_BUCKET_NAME' and 'PATH_TO_LOCAL_RECORDING_FILE'
            s3.upload_file('textbase/distress_audio/recording.wav', bucket_name, object)

            print('File uploaded successfully')
        except NoCredentialsError:
            print('Unable to locate AWS credentials')
        # Generate the URL for the object
        object_url = f"https://{bucket_name}.s3.amazonaws.com/{object}"

        return object_url
    
    @classmethod
    def transcribe(cls,link):
       # this function is used to transcribe the audio file and
       # send the transcript to the responsible organization via twilio
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        transcript = client.intelligence \
                        .v2 \
                        .transcripts \
                        .create(
                                service_sid='ISe08c0e4626c74cac8cef1875c1f8199a', #service sid of the twilio  messaging service
                                channel={}
                            )

        print("Distress call transcripted  & sent successfully")




 
