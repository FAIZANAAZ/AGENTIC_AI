
00_openai_agents
"Sab se pehle LLM (Large Language Model) OpenAI le kar aaya tha, us ke baad langraph waghaira jaise kai frameworks aaye,
 jo ke LLM ke use se agents banate the, lekin woh complicated the. Phir OpenAI ne Swarm introduce kiya, aur uske baad CRUAI aaya, 
 jo ke developers ke liye kaafi asaan tha aur viral bhi ho gaya. Uske baad OpenAI SDK le kar aaya jo ke antropit  pr bna he or open sorce bhi he jismy hm kisi bhi llm ko use kr skty hen , jo usse bhi zyada asaan tha."

<!-- https://github.com/panaversity/learn-agentic-ai/tree/main/00_openai_agents -->

AGENTS:
(1) LLM: #********************
Isme do cheezen hoti hain: LLM aur tools.
Agent ek insan ki tarah hota hai. Insan ke paas dimag hota hai aur agent ke paas LLM hota hai. Hum agent ke autonomus action lene wale ek insan hain.


(2) Tools: #********************
Iske paas bohot saare tools hote hain jinki madad se ye kaam karta hai. Ye internet se cheezein connect kar sakta hai, jaise insaan ke paas mobile ya laptop hota hai kaam ke liye, waise hi iske paas bhi tools hote hain.

HANDOFFS:
Yani multiple agents ka ek saath kaam karna. Har agent apne kaam me expert hota hai. LLM Dekhta hai ke jo kaam ya sawal aaya hai, usme kaunsa agent expert hai. Jo expert hota hai us kaam me, usko kaam handoff kar diya jata hai, yani de diya jata hai.

GUARDRAILS: #********************
Saare agents jab kaam karke output dete hain to ye check karta hai ke output sahi hai ya nahi. Ye ensure karta hai ke final result theek ho.

TRACING & OBSERVABILITY: #********************
Tracing karne se ye faida hota hai ke jo bhi agents kaam karte hain, unhone kya kaam kiya aur kis tarah communicate kiya, wo sab hum dekh sakte hain. Sab kuch trace ho jata hai, to hum decision le sakte hain ke sab sahi hua ya koi change karni padegi.

<!-- $************************$ -->

PYTHON FIRST 
   hmy phly python pr peojects kam krna hota he best practice sdk me python first rkha gya he ke ap python me agents bnay 
 
Built-in Loop #***********************

agent loop ka kaam yeh hota hai ke ek agent repeatedly apna process chala sakta hai jab tak kisi specific condition ko meet na kare ya desired output na mil jaye. Yeh loop agents ke andar automation aur self-improvement ke liye use hota hai.

Kaise Kaam Karta Hai?
Task Initialization: Pehle agent ko ek task diya jata hai. Yeh task kisi user input ya kisi external request par ho sakta hai.
Processing & Decision Making: Agent apne LLM aur tools ka use karke data process karta hai aur decision leta hai.
Execution & Feedback: Jo bhi decision liya jata hai, agent usko execute karta hai aur result ko check karta hai.
Loop Mechanism: Agar result incomplete hai ya required outcome nahi aaya, to agent dubara process start karta hai. Yeh tab tak chalta hai jab tak desired output na mil jaye.
Example:
Agar ek agent ko kisi user ka sawaal samajhne aur uska best jawab dene ka task mila ho, lekin pehli baar me sahi jawab nahi aya, to woh apne process ko repeat karega, naye tools use karega, ya naye queries generate karega jab tak accurate response na mile.

Agar koi specific condition set ho (jaise maximum retries ka limit yani ke loop bs 20 bar chly), to agent usko bhi follow karega aur agar limit exceed ho gayi to error ya alternative action le sakta hai.




<!-- ////////////////////////////////////////////////// -->

-01_swarm # $**************$

Swarm aik experimental framework hai jo OpenAI ne multi-agent systems ko efficiently manage karne ke liye design kiya hai. Iska maqsad yeh hai ke multiple AI agents mil kar complex tasks ko efficiently solve kar sakein. Isme do basic concepts hain:

Yeh autonomous agents + handoff system ka use karta hai taake complex tasks efficiently solve ho sakein. OpenAI ne isko aur improve karke Agents SDK introduce kiya jo ab production-ready hai aur zyada advanced AI orchestration provide karta hai.

Swarm ka design simple aur flexible hai, taake developers easily multi-agent systems bana sakein. Yeh complex frameworks ki jagah lightweight aur scalable hai, jo AI agents ko zyada smoothly operate karne deta hai.

Swarm se Agents SDK tak
Ab OpenAI ne Agents SDK introduce kiya hai, jo Swarm ka advanced version hai. Yeh Swarm ke basic principles ko follow karta hai, magar aur zyada features aur efficiency ke saath.

🔹 Kya Naya Hai Agents SDK Mein?

Enhanced Orchestration: AI agents ko aur achi tarah manage aur coordinate karne ka system.
Parallel Processing: Multiple agents ek sath kaam kar sakte hain.
Better Routing & Task Delegation: Yeh aur intelligent ho gaya hai tasks ko sahi agent tak pochane mein.
Guardrails for Quality Control: Har agent ki output check hoti hai taake final results sahi hon.


Swarm AI Design Patterns
Swarm ya Agents SDK ko samajhne ke liye Anthropic ke kuch important AI design patterns hain jo ye follow karta hai:

1️⃣ Prompt Chaining: Complex kaam ko chhoti steps mein tod kar sequentially process karna.
2️⃣ Routing: Jo kaam jis agent ke liye best ho, usi ko diya jaye.
3️⃣ Parallelization: Multiple tasks ko aik sath process karna taake efficiency bade.
4️⃣ Orchestrator-Workers: Aik main agent (orchestrator) jo tasks ko alag alag agents (workers) mein distribute karta hai.
5️⃣ Evaluator-Optimizer: Aik agent jo system ka performance check karta hai aur improvements suggest karta hai.

<!-- //////////////////////////////// -->

Workflow:
Workflow ka matlab hota hai kisi kaam ko pura karne ka sequence ya tareeqa. Matlab, ek kaam ko mukammal karne ke liye kis tareeqe se steps ya tasks perform karne hain, woh workflow kehlata hai. Jab hum programming ya AI systems ki baat karte hain, to workflow ka matlab hota hai data ka flow ya steps ka sequence, jo kisi kaam ko mukammal karne ke liye follow kiya jata hai.
CHAT COMLITIOPN 
yani ye dekhna ke konsa llm sbsy acha he wo lagana



Agency/autonomy  (AI ya Chat Agents mein):
Agency ka matlab hai ke AI ya chat agent ko apne aap decision lene ki salahiyat ho. Jab ek agent ke paas agency hoti hai, toh woh sirf user ke commands ke response mein kaam nahi karta, balkeh woh apni understanding ke hisaab se decisions leta hai aur actions karta hai.

workflow or agency ka use or differcce koch u he ke hm khi jga hm workflow ka use krty hen or khi agency ka 
jesy hm ak email agent bnaty hen hm osmy ak company ke liye workflow dety hen agent ko ke ye hmari main company he ag iski traf sy koi email ati he to oska ans is trha hi dena taky wo koch ghalat na dede
or isi trha agency hm isi liye khty hen taky koch unimportant emails hen to osmy wo khod decisio lele 

<!-- //////////////////////////////// -->

OPEN ROUTER*****************
openrouter 50 free llm provide krta he ye ak esa pekig he jo apny ander sb llm rhta he phly llm ka use esy hota tha ke hm kisi bhi 
company ka llm use krny ke liye api key janerate krky lgani hoti thi lekin openrouter me 50 yani bhut sari companies ke llm hen or hmy 
key bhi nhi chiye bs ak key lgygi open ai ki or phir bs jis company ka llm use krna he oska model ka name likhngy  wo chal jayga 

<!-- //////////////////////////////// -->


simple code of agent 

from openai import   Agent ,Runner 

aget = Agent(
   name="lahoreTA"
   instruction="Agent for Lahore travel assistance",
)  # Initialize the agent
<!-- sbsy phly agent ka name dengy or instruction yani sytem prompt yani ke is chiz ko dimag me hmehsa wo rkhyga agent har sawal ka ans dety waqt jesy wo yad rkhyga ke hn me lahuore travel ke liye bna hon -->

result =Runner.run_sync(
   agent,
   "what is your name"
)
<!-- runner hi hmara agent loopko chala he  -->

print(result.final_output)
<!-- final output by default func he jo hmy resul nikal kr deta he  -->