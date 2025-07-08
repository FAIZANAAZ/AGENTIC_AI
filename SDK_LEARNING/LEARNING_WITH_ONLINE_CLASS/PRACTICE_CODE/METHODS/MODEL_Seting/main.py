import json
from dotenv import load_dotenv
from agents import Agent, ModelSettings,Runner, enable_verbose_stdout_logging
import rich
from agents.extensions import handoff_filters 



# ***********************************************************


enable_verbose_stdout_logging()


load_dotenv()  # Load environment variables from .env file


agent =Agent(
    model="gpt-4.1-mini",
    name="triage agent",
    instructions="you are a helpful agents.",
    model_settings=ModelSettings(
        temperature=0.1,
        # jb hm minimum temprature rakhengy to wo ak jesy 0.1 0.2 is trha to wo ak jesy ans kry ga mtlb hm hi bolengy to wo ans hello kreyga jitni bar hi bolengy
        # jb hm temprature maximum rakhengy yani 0.7 0.8 ya 1 2 to wo har bar hi bolney pr ans diffrent dega 
        max_tokens=1000,
        # jb hm max tokens 1000 rakhengy to wo 1000 tak ka ans dega yani 1000 words ka
        top_p=0.9,
        # ye 0.9 yani 90% ye har word ki ak probaility hoti he ke isky any ke chance kitny hen jesy i ke bad am any ke to ye sbsy high probsbility ko otha kr wo wod i ke bad lga dega
        
        tool_choice="required",
        # ye by dafalut auto hota he yani chalta rhta he or by default value na hoti he yani na bhi to to chal jayga 
        # agr isko hm "none" krdengy to wo nhi kryga use or requied krdengy to lazmi chalyga 
        # or auto me oski mrzi he chly ya nhi 
        # or agr ksis tool ka anme deden to phir wo osi ko chlayga bhly ga or agr swal os tool ke motabik na hoto wo dosra tool bhi chalalyga kioky osko bs ye pta he hn ye wla krna he jiska nmae diya he use hony bad tool reset ho jata he phir wo sawal ke motabik dosra tool bhi chalaega 
        # lekin agr hm None ye wala krdengy tb wo auto hoga yani chalalo ya nhi marzi he
        # toll use krny ke bad wo reset krdyga tool ko 
        
        frequency_penalty=0.0,
        #  -0.2 sy 0.2 tk hi isko kr skty hen
        # ismy ye hota he ke agr hm 0 sy agr hm 0.2 tk agr set krengy to koi agr esa word he jo bar bar ara he ans me bar bar to wo osko bar bar nhi layga different layga ye zada creativity hogi 
        # agr - 0 sy -0.2 me rakhenngy to wo phir repeat kryga
        presence_penalty=0.0,
        # ye bhi same he lekin ismy word ki jga wo sentence/topic ko repeate nhi kryga or - me kryga 
        parallel_tool_calls=True,
        # ye bhi by default None value leta he or behaviour wo true hota he
        # iska matlb bhly zarorat ho ya na ho sary tools ko call kro 
        # agr iskofalse krdengy to ye nhi chalyga 
        
    )
)
# isko agr run krengy to ismy abhi error ayga kioy ye ak sath nhi use hoti kochapas me conflict kr jati henye bhi same he lekin ismy word ki jga wo sentence/topic ko repeate nhi kryga or - me kryga 

# ***********************************************************

ans=Runner.run_sync(agent,"i need customer support?")
rich.print(ans.final_output)
  

# ***********************************************************
# ///////////////////////////////////////////////////////////
