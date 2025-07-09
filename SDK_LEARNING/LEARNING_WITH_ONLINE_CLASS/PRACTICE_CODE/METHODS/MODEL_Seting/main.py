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
        
        truncation="auto",
        #    ye convesation history ko ccontrol krta he input ka context window yani 1 million words hon bs or output yani max_token 
        # agr ye auto hoga to wo khod manage kryga agr limit sy cros kr jay ya koch bhi agr disable rakhengy to wo limit cros krny pr error de dega
        reasoning={ "efforts": "high" },
        # ye experamental parameter khlata he model seting ka
        # kioky 4.1 reasing model nhi he agr is trh aka model use krengy to phir wo error use kryga kioky wo reasing support nhi krta
        # agr task simple heto hm set krengy low agr normal heto midium agr complex heto high
        ),
        metadata={
            "name":"faiza",
            "class":"223"
        },
        #    ismy hm koch bhi deta ak oobject me  rkh skty hen key value me lekin ye data llm ko nhi jata na hi history me ata he
        store=False,
        # ye by default value none hoti he behaveiaur true hota he
        # ismy ye hota he agr hm isko false krden to iska my jitna kam hm krengy koi response to wo open ai ke server pr nhi trace hoga
        # iska ye faida he ke hm kisi client ke liye application bnaygy to hm osko khengy ke apka dta openai ke server pr bhi nhi jayga to leek nhi hoga
        include_usage=True
        # 
        
        )
        # isko agr run krengy to ismy abhi error ayga kioy ye ak sath nhi use hoti kochapas me conflict kr jati henye bhi same he lekin ismy word ki jga wo sentence/topic ko repeate nhi kryga or - me kryga 
        #agr hmy isy dehna hoto hm result._last_agent.model_settingd.metadata
        #ye runner wala result he jismy ans ata he runner ka agent ke 
        # ye debuging me kam ata he 

# ***********************************************************

ans=Runner.run_sync(agent,"i need customer support?")
rich.print(ans.final_output)
  

# ***********************************************************
# ///////////////////////////////////////////////////////////
