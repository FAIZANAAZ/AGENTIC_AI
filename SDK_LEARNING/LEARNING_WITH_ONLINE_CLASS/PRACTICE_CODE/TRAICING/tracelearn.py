import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner,trace,TracingProcessor,set_trace_processors
from dataclasses import dataclass 
import rich 

# trace ka bydefault name agent trace hota he or hm is name ko change bhi kr skty hen 
# age hm open api key ko use krengy tb hi bs hm dekh skty he open aikke dashborard pr tracing ko 

load_dotenv()

class My_Tracing(TracingProcessor):
        
    def on_trace_start(self, trace):
        
        rich.print(f"Trace started: {trace.trace_id}")

    def on_trace_end(self, trace):
        rich.print(f"Trace ended: {trace.export()}")

    def on_span_start(self, span):
        rich.print(f"Span started: {span.span_id}")
        rich.print(f"Span details: ")
   

    def on_span_end(self, span):
        rich.print(f"Span ended: {span.span_id}")
        rich.print(f"my span😎: {span.span_data}")
        
        rich.print(f"Span details:")
      

    def force_flush(self):
        rich.print("Forcing flush of trace data")

    def shutdown(self):
        rich.print("=======Shutting down trace processor========")
        # Print all collected trace and span data
        rich.print("Collected Traces:")
        
        
        
#  **********************
# ismy hm kisi bhi method pr click kengy to pta lg jayga ke ismy kiya kiya or use hm kr skty hen  or oska kiya kya kam he  iski documentation me jakr   
        
        
      
my_tracing=My_Tracing()
set_trace_processors([my_tracing])

agent=Agent(
model="gpt-4.1-nano",
name="my_agent",
instructions="You are a helpful assistant .",

)   

async def main():
    with trace("faiza exmple workflow"):
        # yha hmy de diya trace ka name 
        result=await Runner.run(agent, "who are u ?")
        rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())






