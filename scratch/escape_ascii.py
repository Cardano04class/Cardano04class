import html

ascii_text = """Ucvnxrf\/ff/\/t//\\/\(tftf/\/f/(\||tffftftfff\ft/fffrrjjfftrjfjjjjrrjrrffrtfffttf//t/fttffjr//fftt/fff/jf/|/t/\tttt\\t\((\t\|/ft)\\\\\/)1)(|)1){)\|(}{1[){1(1())}(11)11}1)){{){{{{))1111)1(){)11()1))({}}){{}[[{1}){{1)]]{((
Uzvnxrjfftf\/ftt/\\\\\tttft//x\{(|/tff/fff/tft//f/tttfjrffjrffrtft/rrf\//\tttt/tt//tjrjttttj//t/jftftjfftfttjtf/fjt\\|t||/\|t/)\\\(|((/(|()|(((|)}})[){1)11|(1[}|)11{}1)){})11)11)(()1){)()})([)){11[{1}}}[1}}}{)|1{1}}[[}{1
Yvuuxxrrf/tft\\/|/f/f/t\tt\\\//|\/\f/ttffjt/f//t///jrfftffttrxjjrtjujtftf/fff/ffrjxffjxjtx/frrt/jffjffft\\tffffjttt\(\j\ffjtftjft/t\\ft/\/\|))()|//\1{{){{1}}1{{{)11{1[})1()1[{}{11)})1{111}[}[}[][})[{{111({1{{(((}}))|}{11
Uzvvxrjf/t//t|\\\tttt\f//|/ttft\\tttf/tftt/t|\\/ft/fffff/tfttftfjfjt/tftft/\trxrjttf/tfftt\ttf/f|txrff/fttjfjfjftfftt\t\(\\tff//))||(||||\\)1\(1|()((}1(){1{}{)11}1()1}1111)1}}{1()(}){{11(}}{}}1}[)1))11){{1})111(1}?[(111{
Yzcunxjj///\///////t/f\(\\tt\//tf//tt//tffff\//frf\ttffjftt\\/tttfjjfjjfj//jf/f/t\/tff/f/tjftttf\ttffjtt|(|/\t/rj//jf|\))fffft//t\\|)||\\)|(((||(\|((({{{{{)1){{)1}}1111{}}[]]]]}[{}}{[1}{}{}{[]]?]}{[}{}(1{1}1}{11}][][[{1{
YXvxrrxfttttf//\tt\\\\\\\/tt/t/tt/t/tt\\\ff//t/fjt/ft/tft|//\f/jjjfttff/trj/fjrftj\/jrjt)|f///)){[1tt\\)1/|)[{)/t\(1[][??1|t|((|/(|1)(\))\\\(((1))(){(){)1(\{1{}{}})]]}]?][]]{1[}{(11{}[111{}}]}}}]}(11[}}?}))1{{11]]?]]]]}}
Ucvvuxrjjftttftttt/tt\tj///fff/t/ff///ttfft/t/tttjfftftj////tt/jrjjfjfrjxrjff/\\\///|){1}1|\(\\t/|)}\//(1[<__>i??>I><~~_~>i~[\\/\|1)/|t|)))\||(((/|))(|{}[[)())1[1]11{1(11111)}{(){][{?{1{){)[[}{{[[1)}(1){1)))1{{[[??]]]]{1
Ucvvnrxjjjf\\ft///tf\\\t/|/ftff/tt\f\\t/tfft/frrrjt/|/ff/fttjttt/|//ttfrj\||||\\(1}1))(1[)\|))}1|/\}[)1[]+!ii+]_i~~I,:;,;l>~~_1)tt/|(t(\\())\)){(1))((({1){)(}11}1}11{1}}11}}{[}1111)1}1{){}{))1[{}}[{11)1)){)11}[][}]][]][1
Uzzuxxjft/tt/\t\/tt/ttffttjtt//ttfft/jtt/rft/jjj///f\ffjfffttttjt|()((())//\fj/}]{{)|(((}{[-~<><?}|[}{1_ii_][\/-__>:,:i~iI,I<~])/||(|/\(\\\(1|t)/1(11{11}{{}[]1{{1)}){{11{[]]11{}})1))1){1}{)[1}}]}{({{1]1))1}}[[]??]]]{[?}1
Uzzuuxjjjffttf\/fftft\tttt//tft\\//ftt/ft/tfjt/tttffjfjf/jt/ttff|]{jtt\{((|tft(1})({{)\\)[--+>><-}}?[]?-+<<_}||}-_!;:;:;:,I>!>-]\\/|1||1||\/\1||/||/|)(1|}1{}}[][(}}1[[{1}}]-?{?]?-{1}}{{1)}]}{{{1((1{[){{111([]]]]]}}]}{1}1
Jzccnxrjfft/ft\\f//t\tt\ttf//\\|\\/ftt/tt\tfjjttjr\trr/tj//tjjtj([fjfr\/|/(()|/(}-{(??}[?+--+_]?[][]--?__++][_~<<ilI,l>iii!l,;~[|\)\(||(|(|(|\)))1)11())}}(}[{]]}{}[}?-??{[[?][][[]]}1}{111{}[[??}}}}{]}11){}{[{[}}}}{1{}{{1
Uzcvnrrjfjf//t||\/\\\\/t/ttttf/\jtj/j\\/tfffftttjffffftrftrjjjjj(|xrrf/t///__(\{}~]{?<-?+_?-?+~+-?++-]}[?_-_~-++>IIli<<>iI,"^,:~?[){1[\1((|((|)()1)[]{1{[]]}]]?]}[}{]??{-?-?][]{{[]?]}1{{1{{1[[[{1{{{{]]}{}}[1}1[]]]][{[)}}[
UXznnrxjt/ttff///\\\/\t/tfttf\t//ttft///tf/ftft\jtfjjtrj\jf/rjjt|{trff|t/tt]?_+>>_i!>l<--]i<i<<_+_!!><??{_~>>ilIIll!il;l:I;,^'^`,>)){}1(1(||1{}]1})(){[1??]?]??]?-[][]?_]_-?][]]]]][]}{[}}{}]{}})1{{]]]]}{[[1}{{{}1}{[[[[{][
zvunrrjjf/ftt//t\/\\\t\/t/fftf/tfttt\\\|\\fffftttfj/fjj\fjtr//ff1\ft\|jxff|1}]+<+>lII~~?i>!~?]-<><>ll<?}]i><~>>!lllI;;:;,:;;,,,,,;~]}1(1)[}{1}{{{?{}{[-?-??-?????[???]?]?-?[[}?[[[[[}[{{{{{{{{}}}]]]}]{1)}{{{[}[}}[}}}]]][1
Jcvunrrjfttttf/\|(\tt|/ftf/\t|///ttff\\\/\/\/fjf/fjjfjttjfjtftffj\}1||)|/({1)[]_+<l!<_})]?<~-{[?_+~+_~I~[[>>><!",";l:",,::;;;;:;;,,Ill+[}][1{)1)][})[1]-]]]??]]]?]}?-?[[[[]}][}?[[?1)[[][]]1}}}[]-[}?]]]?}{(1)}{{}1{]}[}]})}
Jzcuxxrff///tf\//\tt/\/t/\ff/|tttfff/\\\/\\/fft//ftffffrj/ftt/fftt|1)|1))){){}_<l^"i+{|]-}]+~<~!<-[\?<+>]?+i!!!",":;;^",,,,,::,,Ill;:::l?}(|{11)11}}})----}?]}[}}]?[][}]}}}}[{]-]]][[[{]}}}{)[][?[[]]}?]]{[]][]]{]}[{{{[{}]{
LXcunnxrrft/tf/tft/tt/\t/tttffftfftt\\/||/\\fffft/fjt/tf|/frf//\fjj/1{/1(1{??+!:":![/|{}]]~i+-<!?)1+>>+<<!ll;i!"::,,"`^^,""^"",,,I;",::^l-?1?|1{[}1111?-[??]][}{}}}{[]]}[[{}{}}]}{}{]}]}}{1{{}}?]]}[}{}}1[}[]][1}?]}[-]{)}}{
Lzvvunrrrffttf///\//\t/t/tt\t/tt/\/|(/t\\t//t//jjftftr/tftjt|1|\/\\{(//|{[--~>I,;;;<]((}[?+~>~I!_->I:IIlIIl;:,"^^^^^,`^`",,"^"``"^`^^^"":!~[}{}[-[}}[[1}}?-??[}[]]]]}11[{{}{}}[]}}[]}-}}[]{][}}}}{{}{1[]{[11[[]}}{1}}]]}{[[?
Lzvcuxrxjff//tt\\\tfjr/t/\tfft/tt\\\\\\t\t//ft\/fjtttjttjjrj/}1){//{1\|(}>!<+<>!;II:l+]}[t_i!lIIiIl:ll::,I;:"""^,`""^,''`^""``'`"^"^.^"^^^;Il~_[?[[[[]}[}}-[[]?]?[]}][}[}[[}}?}]}][[]]]??[[??]-}{1}}{{}}}[1)}}}}[}11[}]{1{-}
CXcvvnrffjtjjttt/|//t/tt\(\ttfftt\|ttt\f\tftff/ft/t/tjjjt///ff1{{{}?[{[]<>li]~<ii;,;!<+1_<lI::l;:I~?>!I,liI;"""^;,:,;^.'.^^`'`.'^`^``'^";:",;^`:>_?]?1[}}[][?-][]?}?[?[][]]???]][}-]]]?]][]]?]}][[}{}1{{[{[}{{{{{[[1]}{}1}{-
Ccvvvujjfftttttt///tttftt\//t/\ftf/||/\/\/t/ttftjftffjfttttjj/){{{[?+~<!I:I]?<~ll:li!+-<~~_~~>l;l>,:!I::Ii!l;"^`'^`^"''''.`'''.''`,:",:;:`^^",^"^!--]}][[]}]]-]?-[]]]?]?[]??[]}-??-?-][[]]}?][]??--]}{][[[[[11}}[{{1{{}}}}}}
Lzzvuxrjfft/fftfft|ttt/\\/\/\\tfffftt//t\t//tfttfrjjffjf/|txxf\(}[?+!:",:,+?+_iI,"li>-}i~])1}}~l::,"":,:I<il",,^`^`^^.'''..``'''^"!!i!il"`^",::,:":i~+-]]]?]][[?[]-?]?]?_??]??]]-??]-]][[{}}}]}}1{?]{1){]{[{}}1{{{}{{}[}}[][
QXcvuunrjrtfjtttttfjt//\//ft/t\r/\/\j\f/\\\\tf\ffjjf/ttfjt/ff/(1[_<l::::I~_+_>:"":l>+[))!!-1)()~:,""``::I~~l"<^'^''^`""^"^`'``''"!>>>!!^"":":Iil;""",>_+-?-][?[]]??_+-??--]-??]][]-__?]]]-]][[[[?]__]?]]-[[{}]}{1{{{11}[}}]}
Yzcuxxrjf\|/ttjjff/|\\|||||//fftjj/f/\ff//tt//tfjftt///())[11]-~_-?-~~<+<->>^:",Ii~></jx|l"``"^^,i_>>:!>]-~-I^",_><;'``````.```^,:;;l;^^,I!<!>;,""^,"'i?-?]??_?-?+~]___?_????]?--?]?--[]}[]-]]-[[??]?_-]}}}1{}}}}[}}]]]}]}}
OJYzunxrjfjfjf/ft\/\tt\//|\\//\|\\\/t//tttf/\/t//tfjt/{]}}-+?+-++~~____+>>i!,:::;:i++_-??-~!:;;;]xnx|?+!i<~>Il,~_}[l^^.'.'.'''..``""::`'`;l!l!:,"^^,:"^`i__--+--~<--+~+-_??--?-?]?]]]?_-?]--_??_]]-]-??}?][]]][]][}}}}}[[{[}
mJXzvnxxxjttfrjjt//\/tfffftt/\\//\t/t\/|/jjtjtt/fftj/|}-]]-+]?_>>~~<~!!~>~iillI;<!]\({((1_[{/(I{vzuzzcvut-i;^<I[?[<I,^^'`'`'...'.'`^""'`:Il;I,,^^```",""`<>+~>+~~~<<++++-_~-+____+_?]?-]]?-?-]_-?[]-]??}[}{[[}[]?]}}{}]]}[{}
WZJXvvxrrrjj/jjjttt/fftfj\/ttft//tff///\/f/f/frffxnf/{[|][~?~!!<~_____~<>_<~llI+_)fncx\|/\1?~)uzYUYYYYXzvfj?II<>!;^`^^,""^^^'..'...''''^:,^:^"`'^.`'```^^:~~+<<<~~<~~~~~~~++++<<<+?-_+-_-__?+___]?-]??[[[}]]{[?][-[]-_-?_??}
%MCXcnunrjffft/t/\tttfjt//t/ttt/t/tttt//tft/tfjftrrj()/|]][\~~_++__~~<i-?<<>!i<_|jucXXXXvxxnvXJUCUUUJJUYYnnx\-~I:^^"^l!!;::"`^``... ...``'`..`'.. .`'``"`"!+~~>~>~<<><~~<~<<~+<~<~_+~~+~+__?[?--?-?--]?[?[]}]]]]]-[[?}][?[[?
oCzcnxrjjftttt///\/t/t//f\fftf/tff\\//ttt\t/ff|\f\|{|/[[-[{!>[}]--]]?_~>ii!ii~(jvYUUJCCJJUJJJCJJCYJJUUYYzvvvf[}}-++~+_>iii:,I,",,"`''`.  .'''.'' ..'`'``^"i<<~<~<<<~<~<~><<<<<<><<<~~~~+~___???-_]?[------??--[}?][}}[[}][?
dCUzvuxrjjff//\ftt|\/\t///\t///f/tt/tfttt/\//\\/t1(({\[[]]}>~-+1}?-__~<i><<ll![xvXUJCCCCCCCLLLLLLLUJJJJUUYXcvnj1}1{{1}}__~i,ll;Il!I!,^``''``'`''.' .  ^..``l>><><<<<<i>>>>><<>><~~<+<~+<~~___-?_-+-_-++----?__?]--??][}[}{[]
ZUzuvvnxrjjjjfffftfft\\///\t///ttf/tt/tttt/\//|t/||?[}[{--+??[(]-??_?-+<<>II+/ucXYUJCLLCJLLLLLLLLLCJJJJJUYYzzcvx|1(/|/1)[->i>!:::""";,,'",``'``..'...'.`'.":l>>!>>>i!!i>i>>><>><~<<<<~<~+<<<~<++_~_++++_-??_]_-?--__-?][]][-
OYzvvnnrjj/ftftttt\/\/\\/\\///t\/fttjftt/\t/jrjjft(][-?}[]--{}}{)}?_~<~<<-[|xczXYUJCCCCLCJCCLLLLLLJCJCJJJJUYXYXcvxf}}1{[[??_+<~I,,^```^````.`'`^'.'.. `'.'.,>!!i!>!>i!>!ii>!iiii>><~<<<<<~~~~~~<~<+_+~~++--_-?-?-__?-----+--
0Uzzvxunjjttfff/tt|//tft|\/\t/tt\//t\tt/\\ft\tt/\/{?}[-+_}1){}[]?-~~<~><-(tuczzYJCLLLLQCLCCCCLLLLLLLJCCJJYUUXcj/|}{?{]]?~+~!~~~ii:,```'''``^`'''`.'..'`'`.',ll!i!i>ii!!!i!!liii>><<<~~<~~++~<~+~~+~+~+~~~~_-_---_--?--_+]]??
0Xzvvvurfftttt\|\/|t//\\\\\/\\tt/\ft\/\//t\/ttt\/((1[[?<<{\/\|1[_~?~-ii-/junrxxcvxujruxrXcYYJCLLLLCJJUYXYXcuf(([-~>I!!!>llI;;!l!i>>!:``''`'''.`' .''. .'''.,;ll!!!!ll!ll!!!i>>>>>>><<>>~~~~~~<<~+++_~~++~_--?_--?-_++_--___?
YYzvunxrjjtf//f\t\\ttf/|\(/tttt///ttt/t/|\\tt/ttt/[??]-~<+?[{1}~_[}]~l+1/t)(\\|||(//({[1/fvuXUCCJJCJYYYvzzr/[1_+?-?-~+><_-+il;:,Iiiii:""`'`''''.. '.. ....'"":;IIIIlIl!!!ii!ii>>>>>>ii<<~~~~><~<~~++++++~__+++_+___++-_-+-_?
0Yzvuxxjf/ftttt/t\//\t/t|\t/t\/t/\/\f\/|\///ttt///\(}}[]-?}]-[{?-{?~<_(((fnvcrxrjbdnxrx/)1(jcXJJJJYXXzzvvf\r\q)\ttfjjjjt\)1][?>;,,li<>I`^''.'.'.`'`.''.'..'``^^,::Il!lI!!!l!><>>>>i>>i><<<<~<<~<~~~~~~++~__~+__~_~~-+_______
0Ycvuxxjtt/t/\ttt/tj\/\t\\\t/t/t/t\//\f///////\/ft()(|111}}?]??-?1(//|jjuUCUJCJJCJ8CXXYUYX\)1tunnr|{}}1|\}]f(u//frrxxxnxrft([[]?l,,```"^"`^'`^`^`'''`' '.'''`^^"",:,IIl!!!!!iiii>i<><>><><<<<>~<~~~~~~~~~~~_+__+_+_~+___--~_
LXcvnxrjfttfftf////t\tt/\|//|tt/\t//t\f/\||/\|//t\|{?~i><__]]?tmtw\|rvzJLLQQQLCJUXChccuuvcYr{{|||)]+I<|/?--{{)|/tfjjfftftf/\()[?{~:,","^`'...'``''`"`.'. ..'^^^`^,"^:Il!l!!!ii>>>>>i>>><><>>>>><~<<~<~<<~~++__+++~~~~~~~_+_-
JYzvnnxrjfttt/f\//t/\\\(|t\\/tt\|\|\/t/tft\\t/t/\//\[+IIII";<_|||\|tLJLQQOOQLLJJYXvunrrxnuvz)[-\xXcv/)({<+-[{{(\ffjf\\)1}}(1)1}[][""^>I^'........'''..'. `.'`"'^""":",ll!!i!i!!i!iii>>>>>>><><<<<<<~~~~~~~~+__~~~+~~~~+-___~
fYzunnxrjt//t/|(\\|/\/\|\|//||\|//\t/|/f|/\/|\\//t/f1-?++>>-{(_]f/t0mwbm0qZLCXUYXzujt|))\jnvr}juJQJcj(1<+<?[}|((|(<!!;<+]---]{{{}[,">>>;`'.....''^.`'..' `. ^^^'`^",",I!!!!!i>>>><>>>>><<<><<><<<><<<<~<<~<~~~~~+~~~~~_++~+~
nzvuuxrjjtttttttt\/\ttf/(\t|/\/ttt//\tf\//t//t/\|(||(1_-<!+\(x~?xn\QQQLLCJYXJCz|--]l;<}}1\jcz?cuOOJvf{]~+if||[_(X++1`,::~Il>+-?]]1^i+l!l:` ..''''.'.``...`^`'^^'^^`"""IIl!!!iii>>i>>>>>>><<><<<~<<<~><<<<<~~~++~~~+++~+++~<~
nYzvnnxjfffft/||\/(/tt////|\/////t//|\\\(\||/\\\/\\/||-+il-|)/_<)r|zLQLJJzzu1]cY-j{:i!f/})fvz~rLZLzn/1_]~}|{[)juUxlI`I;]-+ill<_?]);[]<ii!:    ... . ....^``''`"""'^"^:,Il!!iiiii><<>>>>>>>>><<><<<~<<~~+<<~~~<~~~~~~~+-_~<~~
uXzvuxxjffttfftt/\|/ttt/|/\ttftft//t/|(t/|/\\\||/\\/t|}-i<;]}?_+-JUrwmO0Unfnxxrrrnf||\\|frcXx{Jwm0Xj\)}+~]1|/|\/trjj//\/(()}?-?[]]11}]>>:,'.  .  ... .'.'''`^^```^^^^,:l!liiii>>>>><>>>>>>>><<><<<<<<~~~~~<~~~~~~~~~~~~~~~~_
uzcvvnnjtfttffft/\\//tt/t////tftf/\/tt/\/\\/\\/\\\\t|//(<!I+)[+i)mwvCwO0QQQQ00QJCYcnjfffrncU+JwwmQXf(){]<[11(|/t///tftt//(11)||))?)1}[+<i:"'....''''.'.'''`^`^`"'^^`^":;I!!!!!i>>>>>>>>>>>i>i><<<~~~<<<<<<~~~~~~~+~~~~<+~~<+
uYcvunxrfjft|\\\\t\\//t/\\ft\\/tt\/(/t\\\\|f/\(||\/\|/t\|/\?}-_?xmqqUZmwO000LCUXzzzvnuuvXYJ)ZwwwmQzf({11]<1|(||/tfftftjjrxxjrrj\1)))1]-~i;^''.''`^:^...'`'`'`^`^^``"",,Il!i!>!i>>>>>>>>>>>>i>><<~<~<<~+~><~~~~~~++~~~~~~~~~~
cXcvunxrfjtftt//fttt\\t/t\\\ttft/\/\\||\\||\|\||(||||/\//||f|}\xvmqppQUmmZOQQLCJLCJUUJYCLYfmwwmmZCvr(111{}_-|//ttfjjjrrrrxnxxt1/|(11{[_<!;"``llll;!!'.'.'`'`^'`'^^^^"",Il!!ii>>>>>>>>>><>>>><~<>><>>i>>><<+~~+~+~~<~~~+~~<<~
uUXvnnxrrjftttt/tft|\/\/t///f/f\t\|f\||(\|\t\\()/\\\(//\|/\Lz|{jnwqpqqwLJZmO0LLCCCCCCCLzxcmwmmmwOJzr/)11)11}?-{rjrnnxnnnnxx(/rt/)1{{}]~<iI"^;li!lll<,'``'``^''^^""^"""^,I!ii!>>>>>>i>ii>>>>>>~<<<<<<><<<<<<~+__~~~~~~<+~~<<~
vXcvuxrxj/ttttt\/\tt\/\\|//\\//t/\||(|\\/t\/(|||/|\\/t|t||fLnrunnmwpppqwmZCXUCCCCJUznnvz0mmwwmwm0Czvxt){1))(||({}{1)((((/jjfft|(}[]]??_<i!:,l!i!!!!_l..^`^`^'```^^^^^",";Ill!>>>>>>>i>>>><><><<<<><<><<<~<<<<~+~~<<>~+~<~<~<
uzcvnuxfjjtt////ftj////(/f\|/\tf/|t((|\|//(|(\|(\f/|t|\\\/xZnxzvnwwqqqqqqwZZ0CJYYXzzUCOmwZOZwqqZLCYzuf\1)\\(1|ffjrxnuuvvuvvunrrj|)[}}[]~>!;,:i<<!Il-;.``^'`'^'"^,^,^^":,:l!!>>>>>i<>i>>>>><>><<~<><<<<<~<~~~<<<+~~<~~+~++<~_
uzcvuxrrjrrf/tt//t//t\||///|\\\\/|\\|\t|//\|||\\\\|\/|/t/|fOvuzOUmqpqqppqwmmO00LQQLQOZmmmqwqpppmQCUXuj/|/tf\)[)fnuuvczcczcvcnnrj\(}[}[?~!I:;I!<~il~l^'``.`^'^^```'^"",":IIii!i><>>>>>i>><<><<<~~~<~<<~~<<~<<<~~~~<~<~++~~++~
nXzvvnxrjf/t/ttf\\tt//t//f|t\|\f/(\||/\|///|\\/\||/\\\||//\JCxYq0ZpppppppqwwZ000QQQ0OZZqpwmmwqqwCUYXx\({1(\/1?]/jnvzXYXXXccvvuxr/|{[[[_<lI:!!l!~>l~^.``'^``^'^"^""^",:":;l!>ii>>>>>>i>><<>><<<~<<~><~~~<><~<~~~~<~~~~~~+~<~
uYzcvnrrjjt\tftt\/f/////////t\\\/|\(||\|\/t|\\/f//f//f/tjt/fmULpQQpppppqqwwmZZO00Q0OZZmZ0Xnr)}umLYXct>;:i]{]_?)ffrnvzzXXcuvvuxrf\([_--+i!;;>>!l<<<!'.^.'^^`^'"^^,^"",,,:Il!!!i>>>><>><>>><<<<~~~<~~~~~~~~~~~~~~<<~+~<<>~~~~<
uXcunnnxjfttt///\t|t//\t///\|t/\/(|\((/\|/|||//t//tf/f/\\\\/nwZwQOpppppqwwmmZOOQLLQQZmwwZZOmOZOO0Ycx?-[[1){)||\\tfrxnzzzXcvvxxf/({}?+_~>l;;Il!i><!^'^'``^`.^`^^"^^",,,",;I>i>i>>i<>~<<<~<<~<<~<~~~<<~~~~~+~+~~~<+~<~~+~~+~+~
uUzvnnrrftt///\//\/t\/\|//|\\\\\\/\|/((\\t/(|\||//ftt|ff\t|\\XqwQJqqppqqwwwmZOQCUUJQZZOZZmmZ0QLJJUnf|||||11((\\//ttfjjrcXzcvnrt({[[_+_<il:I><<<i>;```"`'`''^^"""^"""",":;l!i>>>>>>><<<<~~~~~<~++<<~~<~~~++~~<~~<~~~~~~~++~+~
fYzvvnrjftt//\/ftt\\/\/\\|||tt///\\||(t|/|((||||\/\///tt//\/trmpwLZppqwqqqwwOCXvXC0ZmwwwmwO0LCJUXcunrxrft(|1(||\\\\ttfjjjxzzux|{]_}?]_+i;;!~~<>>i''`^`````"^^"^,^^",,:;Il!>>>i><>>><<>><<<<<~<<+~~~~~~~+<~+~~<~+~~~~~~~+~~~~
uXzcuxrjfjtt\\/\t/\(((|\\\f|\t\/\|(\|\/|\\(\\|\|\\tft/ff\/\\t/OwqmOpqmqqqqqQXjzUCOZZwwZmOO0QCCUUzvvvcunxrft/(|(1()(((\\ffjfvcn(]-]{{{}+i:I>~<>>;````^^""`^^`"^^^^^",:,;l!iii>>>>>>~<<<+<~<<~<~<~~~~+~~~~~~~~~~<~_+~~~~~<<~><
nzzcuxjjft/t\\/f/\\(/\\/t///tt(\///\\\t/|\///ft/\/tt\ftftt\\t/uwpq0pqZqppqOvjUJLL0OZmqmwmmO0QLCCUXzczvuxxrjf\|((1)(11)1)}(ttYc\-_{/|)}~!:l<~<!,^``^^"'```^```^^"",:,I;Il!i>>>>>>>><<><<<<<~~~~~~~~~~~~+~~~+<~~~~~+~~~~~~+~+<
xXzcvxjrjttt/\/f\\/\\\\|\/\//((\||/|\|||\/t/\t//\ttt\/|////ttttnmq0qqmZpqqLfzLCUULZmwmO0CJUYXcuxxxft/\\|()1]-]_~!!IIi~_ftjx\Uc(+-/t/({~l;llI"``'`'^"`''``^`^^^""",;;;I!ii>><<><<~<><<<~<~~~~~~~~<~~~~~~+~~+~+~~~~~~~~~<<~<<>
xXvvunrj/ftt\t/t\\/|\\/\\/\|\|(|/(|\\/\///t/(/t//////t\tjj\||//tnqOqpwZwpq0zn0Ccj]+>[/umJJmOYmOOCXYCUYzrvzu(0x_}!;::+tffrxfYUx]~{tf/)?<;^^^`^^``"^^`^^`"^^,`""""":II!!!i>>><<i>>>~<~~>~<<>~~~~~~~<~~~~~>~<<<~~~++~~~~~~~~><<
xXcvvjjfftttt\ft\\\|\\|(||\(\\||/(\t\//\/||\\/t//\//jt|jt/\|///\/tjZpqwwppqLcLQJJJJf}t0pmZdpmkpqqQZO0CYcuzu)jj-][[{/\tfjjjUJv|_-|f\([+!:`"`^```^^`'``'^^`^`"^,",;:Il!!!>>><<<<~>~~+~~<~~~~~~+~~~~~~~~~~~~~~~~+~~~~~~~><<><<<
uXvvvnrffttt//t\\/\||||/\\/|\\\\\/t\//|/|\/tftt/|/tt\/ttt///f\t//ttXppqwqppwQX0OZ0QmQJJCUYXx(L0LJx(jrj/{()()1{[[)((//ttfjzUz|--)//|{_>;""^^^^^```'`^^`^`^^^"^",:;IIl!iii>>><<<<>><~~~~~~++~~~~~+~~~++++~+++~~~+~++~~<>><~><>
uJcvuxrrf/ttf/tttt//tttttt//\///\//tt\/ff/t\//tttjtt//t/f\f\ft/\\/jn0pqqqppqwCCZZZO0qwZO00QCJXcvcvuvcvvxf|(1[[{11(\t\\fjXYv(+]{//)}-<!"^""^"^`^^^^"^^^."^^^`^^,::li!i><>i>>>>>><><~>~~~++++~~~~~~+~++~~_~~~~~++~<~~~~~<>>~>>
nUccurxjtft//tt(/t\f///ttt//\|\\\|\/tt|\//////ttftt//(\/t///jtf/t|ffzmqqqpppqm0ZwwwmmwqqmOQUUYzcvununrf/(11(|(()|/t\|tjvzx?-]}\|1}+>l:,"""""""^^,^,,^`^^"`^"^,,,:Ii!!>>><><>>><>><<~+~<~~<<+~~~+++~++_+~+<~~~~~+~+~~~<~<<<~>
xXcuuxxjfjjf///\\/\|tt///\|\\\\\\|\tt\/\/\||\ttf/j/t/|t\tf\tfttf\/t/jJwqpqpqqwmmmwwwwwqqqwZOLJXcvcurfffrjjf/|(\/t/\/ffnu\--]1|){]+<l:"""^"""^""^``^'^^"""`",`,;:I;!!ii>>>><>>>>>>><~~+~~~~~~~~+++_++_~+_~~~~_~~~~~~~~+~~~~~~
nUzvcnxjftt\\t\/////tt/\\\\/|t/(\|/(//\/////|\fft////\|/\\tf\/fttt\\fxLwqqqqqwqqwwmmmmwqwmO0QLCUUYXccvunxjfft/t////jtjj|--?{{{}?-<!I:,"",""^"^^^`^^"^"^"^""^,:;Illl>>i<i>><><<>><~<~<~~~<~~~~+~~+~+++~++~~+~~++~~~+~+~~~~~~~
jUzunxrjttttjftt|\/\/t\t|\tf////\/|////\\\\|||/\\||//f/\(\|\ftt\\\\tt\rOwwwqqwwqqwwwmmmwZO00QCJUUXzccvvnuxxjfft//\/tf\[__?[}[[]_+<IIl,^,,""""^","^``^^^^^^^,::;I!!!>>>>>>>><>>><<<~~~~~~~~~+~~~~~~+~~~+_~+~~~~~~+~~~~~~<~~~<
fUcvuxxjjttttt/////\\tt/\\|t///\\\//f\|\|\\/\\|\\//t\t(|||//tt/\/\////rrCwwwmZwwwqqqwwZZmZQQQCCJYYXzccvuunxrjjj\(\/\)]+-?][]]]-+>!l!l:,:,",,",^"^`^"^'^"^"""::Il!!yyyyyyyuyyyyuuuunxrj|)[}}[]~>!;,:i<<!Il-;.``^'`'^'"^,^,^^
"""

escaped_tspan = ""
y_offset = 60
for line in ascii_text.strip().split("\n"):
    escaped_line = html.escape(line).replace(" ", "&nbsp;")
    escaped_tspan += f'<tspan x="25" y="{y_offset}">{escaped_line}</tspan>\n'
    y_offset += 6.5

with open("/Users/macbook/Desktop/Cardano04class/scratch/ascii_escaped.txt", "w") as f:
    f.write(escaped_tspan)
print("Finished!")
