import os
from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
import chainlit as cl

load_dotenv()
set_tracing_disabled(disabled=True)

OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

if not OPEN_ROUTER_API_KEY :
    raise ValueError("OPEN_ROUTER_API_KEY is not set in the environment variables. Please set it and try again.")

history :list= []
# ***********************************************************
models={
    "DeepSeek": "deepseek/deepseek-r1:free",
    "Gemini_2_Flash": "google/gemini-2.0-flash-exp:free",
    "Mistral": "mistralai/devstral-small:free",
    "Qwen": "qwen/qwen3-14b:free",
    "Meta_Llama": "meta-llama/llama-4-maverick:free"
}
# YE KEYS HMY WHI SY MILENGI JGA SY YE OPEN ROUTER KE API MILTI HE LLMS KI
# ***********************************************************





@cl.on_chat_start
async def start_message():
    await cl.Message(content="Hello! How can I help you today?").send()
    
    user_selected_model=await cl.ChatSettings(
        # ye hmary chat me jha chat krty hen wha seting ka ak option add ho jayga 
        [
            cl.input_widget.Select(
                id="model",
                label="Choose Any LLM Model",
                # ye ak normal heading he jo user ko dikhana he
                values=list(models.keys()),
                # YE WO model ki  OBJEC KI keys pass ki hen hmny list me 
                initial_index=0
                
                # iska matlb ak by default 0 pr jo he wo slect ho jay 
                
            )
            # ye hmy bna kr dega ak selection bar
        ]
    ).send()
    
    await on_model_update(user_selected_model)
    # taky variable ko function scop sy nikal sken
    
    
# ***********************************************************
# jb user koi model chhange kryga ye function khod call hoga
# ye hmny bs screen pr name dikahny ke liye lgaya he ak message deny ke liye user ko  
@cl.on_settings_update
async def on_model_update(user_selected_model):
    model_name=user_selected_model["model"]
    # hmny model niakal liya yha idke zariye 
    
    cl.user_session.set("model",model_name)
    # hmny user_session me model_name niakal liya agent me pas krny ke liye 
    await cl.Message(
        content=f"Your selected model is {model_name}.👩🏻‍🚀"
    ).send()
    
   
# ***********************************************************
    
    
@cl.on_message
async def main(message: cl.Message):
    question =message.content
    history.append({"role": "user", "content": question})
    
    model_name_get=cl.user_session.get("model")
    
    client=AsyncOpenAI(
    api_key=OPEN_ROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    )

    
    agent =Agent(
        name="practice agent",
        instructions="you are a helpful agents.",  
        model=OpenAIChatCompletionsModel(model=model_name_get,openai_client=client),
        
       
    )

    
    answer = Runner.run_sync(agent, history)
    # or jo agent ans kryga wo answer me aa jayega yni Runner.sync m or final output sy hmm dekhlengy 
   
    print(answer.final_output)
    
    # ab hm chahry hen ke hm is ans ko ui pr dikhaen 
    await cl.Message(content=answer.final_output).send()

