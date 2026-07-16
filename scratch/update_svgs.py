with open("/Users/macbook/Desktop/Cardano04class/scratch/escaped_tspan_v3.txt") as f:
    tspan_content = f.read()

# For Dark Mode
dark_template = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="'SF Mono', Consolas, Monaco, 'Andale Mono', monospace" width="985px" height="570px" font-size="14px">
<style>
.key {{fill: #ffa657; font-weight: bold;}}
.value {{fill: #a5d6ff;}}
.cc {{fill: #616e7f;}}
.title {{fill: #39FF14; font-weight: bold;}}
.border {{fill: #30363d;}}
.term-frame {{fill: #8b949e;}}
.term-glow {{fill: #39FF14;}}
.term-prompt {{fill: #58a6ff; font-weight: bold;}}
.ascii-photo {{font-family: 'SF Mono', Consolas, Monaco, monospace; font-size: 4.1px; fill: #39FF14; font-weight: bold;}}
</style>
<rect width="985px" height="570px" fill="#0d1117" rx="15" stroke="#30363d" stroke-width="1.5"/>

<!-- ASCII Portrait Face Graphic -->
<text x="25" y="40" class="ascii-photo">
{tspan_content}
</text>

<!-- Neofetch Stats Info -->
<text x="360" y="50" fill="#c9d1d9">
<tspan x="360" y="50" class="title">cardano_class@1337</tspan>
<tspan x="360" y="70" class="border">————————————————————————————————————————————————————————————————————</tspan>
<tspan x="360" y="90" class="cc">. </tspan><tspan class="key">OS</tspan><tspan class="cc"> ............. </tspan><tspan class="value">macOS, Debian Linux, Alpine, Docker</tspan>
<tspan x="360" y="110" class="cc">. </tspan><tspan class="key">Host</tspan><tspan class="cc"> ........... </tspan><tspan class="value">1337 Benguerir (42 Network)</tspan>
<tspan x="360" y="130" class="cc">. </tspan><tspan class="key">Kernel</tspan><tspan class="cc"> ......... </tspan><tspan class="value">DevOps &amp; Systems Engineering</tspan>
<tspan x="360" y="150" class="cc">. </tspan><tspan class="key">IDE</tspan><tspan class="cc"> ............ </tspan><tspan class="value">VS Code, Vim</tspan>
<tspan x="360" y="170" class="cc">. </tspan><tspan class="key">Uptime</tspan><tspan class="cc"> ......... </tspan><tspan class="value">Active Software Engineering Apprentice</tspan>
<tspan x="360" y="190" class="cc">. </tspan>
<tspan x="360" y="210" class="cc">. </tspan><tspan class="key">Languages.Prog</tspan><tspan class="cc"> . </tspan><tspan class="value">C, C++, TypeScript, JavaScript, Python</tspan>
<tspan x="360" y="230" class="cc">. </tspan><tspan class="key">Languages.Dev</tspan><tspan class="cc"> .. </tspan><tspan class="value">Docker, Kubernetes, Nginx, Bash Shell, AWS</tspan>
<tspan x="360" y="250" class="cc">. </tspan><tspan class="key">Languages.Web</tspan><tspan class="cc"> .. </tspan><tspan class="value">React, Next.js, Node.js, PostgreSQL, MariaDB</tspan>
<tspan x="360" y="270" class="cc">. </tspan>
<tspan x="360" y="290" class="cc">. </tspan><tspan class="key">Hobbies.Dev</tspan><tspan class="cc"> .... </tspan><tspan class="value">Systems, Homelabbing, Automation, WebSockets</tspan>
<tspan x="360" y="310" class="cc">. </tspan><tspan class="key">Hobbies.Org</tspan><tspan class="cc"> .... </tspan><tspan class="value">DevOps &amp; Frontend @Almalgo</tspan>
<tspan x="360" y="330" class="cc">. </tspan>
<tspan x="360" y="350" class="title">- Contact</tspan> <tspan class="border">————————————————————————————————————————————————————————</tspan>
<tspan x="360" y="370" class="cc">. </tspan><tspan class="key">Portfolio</tspan><tspan class="cc"> ...... </tspan><tspan class="value">https://m-amir.xyz/</tspan>
<tspan x="360" y="390" class="cc">. </tspan><tspan class="key">Email</tspan><tspan class="cc"> .......... </tspan><tspan class="value">cardano_class@proton.me</tspan>
<tspan x="360" y="410" class="cc">. </tspan><tspan class="key">Twitter (X)</tspan><tspan class="cc"> .... </tspan><tspan class="value">@cardano_class</tspan>
<tspan x="360" y="430" class="cc">. </tspan>
<tspan x="360" y="450" class="title">- Featured Projects</tspan> <tspan class="border">————————————————————————————————————————————————</tspan>
<tspan x="360" y="470" class="cc">. </tspan><tspan class="key">ft_transcendence</tspan><tspan class="cc">. </tspan><tspan class="value">Next.js, TS, WebSockets, PostgreSQL, Docker</tspan>
<tspan x="360" y="490" class="cc">. </tspan><tspan class="key">Inception</tspan><tspan class="cc"> ....... </tspan><tspan class="value">Docker, Nginx, MariaDB, WordPress, Alpine</tspan>
<tspan x="360" y="510" class="cc">. </tspan><tspan class="key">minishell</tspan><tspan class="cc"> ....... </tspan><tspan class="value">Unix Systems Programming in C (Pipes, Signals)</tspan>
<tspan x="360" y="530" class="cc">. </tspan><tspan class="key">push_swap</tspan><tspan class="cc"> ....... </tspan><tspan class="value">Optimized Complexity Sorting Algorithms in C</tspan>
</text>
</svg>
"""

# For Light Mode
light_template = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="'SF Mono', Consolas, Monaco, 'Andale Mono', monospace" width="985px" height="570px" font-size="14px">
<style>
.key {{fill: #953800; font-weight: bold;}}
.value {{fill: #0550ae;}}
.cc {{fill: #8b949e;}}
.title {{fill: #1a7f37; font-weight: bold;}}
.border {{fill: #d0d7de;}}
.term-frame {{fill: #57606a;}}
.term-glow {{fill: #1a7f37;}}
.term-prompt {{fill: #0969da; font-weight: bold;}}
.ascii-photo {{font-family: 'SF Mono', Consolas, Monaco, monospace; font-size: 4.1px; fill: #24292f; font-weight: bold;}}
</style>
<rect width="985px" height="570px" fill="#ffffff" rx="15" stroke="#d0d7de" stroke-width="1.5"/>

<!-- ASCII Portrait Face Graphic -->
<text x="25" y="40" class="ascii-photo">
{tspan_content}
</text>

<!-- Neofetch Stats Info -->
<text x="360" y="50" fill="#24292f">
<tspan x="360" y="50" class="title">cardano_class@1337</tspan>
<tspan x="360" y="70" class="border">————————————————————————————————————————————————————————————————————</tspan>
<tspan x="360" y="90" class="cc">. </tspan><tspan class="key">OS</tspan><tspan class="cc"> ............. </tspan><tspan class="value">macOS, Debian Linux, Alpine, Docker</tspan>
<tspan x="360" y="110" class="cc">. </tspan><tspan class="key">Host</tspan><tspan class="cc"> ........... </tspan><tspan class="value">1337 Benguerir (42 Network)</tspan>
<tspan x="360" y="130" class="cc">. </tspan><tspan class="key">Kernel</tspan><tspan class="cc"> ......... </tspan><tspan class="value">DevOps &amp; Systems Engineering</tspan>
<tspan x="360" y="150" class="cc">. </tspan><tspan class="key">IDE</tspan><tspan class="cc"> ............ </tspan><tspan class="value">VS Code, Vim</tspan>
<tspan x="360" y="170" class="cc">. </tspan><tspan class="key">Uptime</tspan><tspan class="cc"> ......... </tspan><tspan class="value">Active Software Engineering Apprentice</tspan>
<tspan x="360" y="190" class="cc">. </tspan>
<tspan x="360" y="210" class="cc">. </tspan><tspan class="key">Languages.Prog</tspan><tspan class="cc"> . </tspan><tspan class="value">C, C++, TypeScript, JavaScript, Python</tspan>
<tspan x="360" y="230" class="cc">. </tspan><tspan class="key">Languages.Dev</tspan><tspan class="cc"> .. </tspan><tspan class="value">Docker, Kubernetes, Nginx, Bash Shell, AWS</tspan>
<tspan x="360" y="250" class="cc">. </tspan><tspan class="key">Languages.Web</tspan><tspan class="cc"> .. </tspan><tspan class="value">React, Next.js, Node.js, PostgreSQL, MariaDB</tspan>
<tspan x="360" y="270" class="cc">. </tspan>
<tspan x="360" y="290" class="cc">. </tspan><tspan class="key">Hobbies.Dev</tspan><tspan class="cc"> .... </tspan><tspan class="value">Systems, Homelabbing, Automation, WebSockets</tspan>
<tspan x="360" y="310" class="cc">. </tspan><tspan class="key">Hobbies.Org</tspan><tspan class="cc"> .... </tspan><tspan class="value">DevOps &amp; Frontend @Almalgo</tspan>
<tspan x="360" y="330" class="cc">. </tspan>
<tspan x="360" y="350" class="title">- Contact</tspan> <tspan class="border">————————————————————————————————————————————————————————</tspan>
<tspan x="360" y="370" class="cc">. </tspan><tspan class="key">Portfolio</tspan><tspan class="cc"> ...... </tspan><tspan class="value">https://m-amir.xyz/</tspan>
<tspan x="360" y="390" class="cc">. </tspan><tspan class="key">Email</tspan><tspan class="cc"> .......... </tspan><tspan class="value">cardano_class@proton.me</tspan>
<tspan x="360" y="410" class="cc">. </tspan><tspan class="key">Twitter (X)</tspan><tspan class="cc"> .... </tspan><tspan class="value">@cardano_class</tspan>
<tspan x="360" y="430" class="cc">. </tspan>
<tspan x="360" y="450" class="title">- Featured Projects</tspan> <tspan class="border">————————————————————————————————————————————————</tspan>
<tspan x="360" y="470" class="cc">. </tspan><tspan class="key">ft_transcendence</tspan><tspan class="cc">. </tspan><tspan class="value">Next.js, TS, WebSockets, PostgreSQL, Docker</tspan>
<tspan x="360" y="490" class="cc">. </tspan><tspan class="key">Inception</tspan><tspan class="cc"> ....... </tspan><tspan class="value">Docker, Nginx, MariaDB, WordPress, Alpine</tspan>
<tspan x="360" y="510" class="cc">. </tspan><tspan class="key">minishell</tspan><tspan class="cc"> ....... </tspan><tspan class="value">Unix Systems Programming in C (Pipes, Signals)</tspan>
<tspan x="360" y="530" class="cc">. </tspan><tspan class="key">push_swap</tspan><tspan class="cc"> ....... </tspan><tspan class="value">Optimized Complexity Sorting Algorithms in C</tspan>
</text>
</svg>
"""

with open("/Users/macbook/Desktop/Cardano04class/dark_mode.svg", "w") as f:
    f.write(dark_template)

with open("/Users/macbook/Desktop/Cardano04class/light_mode.svg", "w") as f:
    f.write(light_template)

print("SVGs successfully updated with HD ASCII art!")
