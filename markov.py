import random
import string 
import re

"""
Create the sample text and the dictionary to store word transitions

TODO: Replace the sample text with a larger text for more interesting results
"""
text = """
Look, I didn’t want to be a half-blood.
If you’re reading this because you think you might be one, my advice is:
close this book right now. Believe whatever lie your mom or dad told you
about your birth, and try to lead a normal life.
Being a half-blood is dangerous. It’s scary. Most of the time, it gets you
killed in painful, nasty ways.
If you’re a normal kid, reading this because you think it’s fiction, great.
Read on. I envy you for being able to believe that none of this ever happened.
But if you recognize yourself in these pages—if you feel something
stirring inside—stop reading immediately. You might be one of us. And once
you know that, it’s only a matter of time before they sense it too, and they’ll
come for you.
Don’t say I didn’t warn you.
My name is Percy Jackson.
I’m twelve years old. Until a few months ago, I was a boarding student at
Yancy Academy, a private school for troubled kids in upstate New York.
Am I a troubled kid?
Yeah. You could say that.
I could start at any point in my short miserable life to prove it, but things
really started going bad last May, when our sixth-grade class took a field trip
to Manhattan—twenty-eight mental-case kids and two teachers on a yellow
school bus, heading to the Metropolitan Museum of Art to look at ancient
Greek and Roman stuff.
I know—it sounds like torture. Most Yancy field trips were.
But Mr. Brunner, our Latin teacher, was leading this trip, so I had hopes.
Mr. Brunner was this middle-aged guy in a motorized wheelchair. He had
thinning hair and a scruffy beard and a frayed tweed jacket, which always
smelled like coffee. You wouldn’t think he’d be cool, but he told stories and
jokes and let us play games in class. He also had this awesome collection of
Roman armor and weapons, so he was the only teacher whose class didn’t put
me to sleep.
I hoped the trip would be okay. At least, I hoped that for once I wouldn’t
get in trouble.
Boy, was I wrong.
See, bad things happen to me on field trips. Like at my fifth-grade school,
when we went to the Saratoga battlefield, I had this accident with a
Revolutionary War cannon. I wasn’t aiming for the school bus, but of course
I got expelled anyway. And before that, at my fourth-grade school, when we
took a behind-the-scenes tour of the Marine World shark pool, I sort of hit the
wrong lever on the catwalk and our class took an unplanned swim. And the
time before that…Well, you get the idea.
This trip, I was determined to be good.
All the way into the city, I put up with Nancy Bobofit, the freckly,
redheaded kleptomaniac girl, hitting my best friend Grover in the back of the
head with chunks of peanut butter-and-ketchup sandwich.
Grover was an easy target. He was scrawny. He cried when he got
frustrated. He must’ve been held back several grades, because he was the
only sixth grader with acne and the start of a wispy beard on his chin. On top
of all that, he was crippled. He had a note excusing him from PE for the rest
of his life because he had some kind of muscular disease in his legs. He
walked funny, like every step hurt him, but don’t let that fool you. You
should’ve seen him run when it was enchilada day in the cafeteria.
Anyway, Nancy Bobofit was throwing wads of sandwich that stuck in his
curly brown hair, and she knew I couldn’t do anything back to her because I
was already on probation. The headmaster had threatened me with death by
in-school suspension if anything bad, embarrassing, or even mildly
entertaining happened on this trip.
“I’m going to kill her,” I mumbled.
Grover tried to calm me down. “It’s okay. I like peanut butter.”
He dodged another piece of Nancy’s lunch.
“That’s it.” I started to get up, but Grover pulled me back to my seat.
“You’re already on probation,” he reminded me. “You know who’ll get
blamed if anything happens.”
Looking back on it, I wish I’d decked Nancy Bobofit right then and there.
In-school suspension would’ve been nothing compared to the mess I was
about to get myself into.
Mr. Brunner led the museum tour.
He rode up front in his wheelchair, guiding us through the big echoey
galleries, past marble statues and glass cases full of really old black-and-
orange pottery.
It blew my mind that this stuff had survived for two thousand, three
thousand years.
He gathered us around a thirteen-foot-tall stone column with a big sphinx
on the top, and started telling us how it was a grave marker, a stele, for a girl
about our age. He told us about the carvings on the sides. I was trying to
listen to what he had to say, because it was kind of interesting, but everybody
around me was talking, and every time I told them to shut up, the other
teacher chaperone, Mrs. Dodds, would give me the evil eye.
Mrs. Dodds was this little math teacher from Georgia who always wore a
black leather jacket, even though she was fifty years old. She looked mean
enough to ride a Harley right into your locker. She had come to Yancy
halfway through the year, when our last math teacher had a nervous
breakdown.
From her first day, Mrs. Dodds loved Nancy Bobofit and figured I was
devil spawn. She would point her crooked finger at me and say, “Now,
honey,” real sweet, and I knew I was going to get after-school detention for a
month.
One time, after she’d made me erase answers out of old math workbooks
until midnight, I told Grover I didn’t think Mrs. Dodds was human. He
looked at me, real serious, and said, “You’re absolutely right.”
Mr. Brunner kept talking about Greek funeral art.
Finally, Nancy Bobofit snickered something about the naked guy on the
stele, and I turned around and said, “Will you shut up?”
It came out louder than I meant it to.
The whole group laughed. Mr. Brunner stopped his story.
“Mr. Jackson,” he said, “did you have a comment?”
My face was totally red. I said, “No, sir.”
Mr. Brunner pointed to one of the pictures on the stele. “Perhaps you’ll
tell us what this picture represents?”
I looked at the carving, and felt a flush of relief, because I actually
recognized it. “That’s Kronos eating his kids, right?”
“Yes,” Mr. Brunner said, obviously not satisfied. “And he did this
because…”
“Well…” I racked my brain to remember. “Kronos was the king god, and
—”
“God?” Mr. Brunner asked.
“Titan,” I corrected myself. “And…he didn’t trust his kids, who were the
gods. So, um, Kronos ate them, right? But his wife hid baby Zeus, and gave
Kronos a rock to eat instead. And later, when Zeus grew up, he tricked his
dad, Kronos, into barfing up his brothers and sisters—”
“Eeew!” said one of the girls behind me.
“—and so there was this big fight between the gods and the Titans,” I
continued, “and the gods won.”
Some snickers from the group.
Behind me, Nancy Bobofit mumbled to a friend, “Like we’re going to use
this in real life. Like it’s going to say on our job applications, ‘Please explain
why Kronos ate his kids.’”
“And why, Mr. Jackson,” Brunner said, “to paraphrase Miss Bobofit’s
excellent question, does this matter in real life?”
“Busted,” Grover muttered.
“Shut up,” Nancy hissed, her face even brighter red than her hair.
At least Nancy got packed, too. Mr. Brunner was the only one who ever
caught her saying anything wrong. He had radar ears.
I thought about his question, and shrugged. “I don’t know, sir.”
“I see.” Mr. Brunner looked disappointed. “Well, half credit, Mr. Jackson.
Zeus did indeed feed Kronos a mixture of mustard and wine, which made
him disgorge his other five children, who, of course, being immortal gods,
had been living and growing up completely undigested in the Titan’s
stomach. The gods defeated their father, sliced him to pieces with his own
scythe, and scattered his remains in Tartarus, the darkest part of the
Underworld. On that happy note, it’s time for lunch. Mrs. Dodds, would you
lead us back outside?”
The class drifted off, the girls holding their stomachs, the guys pushing each
other around and acting like doofuses.
Grover and I were about to follow when Mr. Brunner said, “Mr.
Jackson.”
I knew that was coming.
I told Grover to keep going. Then I turned toward Mr. Brunner. “Sir?”
Mr. Brunner had this look that wouldn’t let you go—intense brown eyes
that could’ve been a thousand years old and had seen everything.
“You must learn the answer to my question,” Mr. Brunner told me.
“About the Titans?”
“About real life. And how your studies apply to it.”
“Oh.”
“What you learn from me,” he said, “is vitally important. I expect you to
treat it as such. I will accept only the best from you, Percy Jackson.”
I wanted to get angry, this guy pushed me so hard.
I mean, sure, it was kind of cool on tournament days, when he dressed up
in a suit of Roman armor and shouted: “What ho!” and challenged us, swordpoint against chalk, to run to the board and name every Greek and Roman
person who had ever lived, and their mother, and what god they worshipped.
But Mr. Brunner expected me to be as good as everybody else, despite the
fact that I have dyslexia and attention deficit disorder and I had never made
above a C– in my life. No—he didn’t expect me to be as good; he expected
me to be better. And I just couldn’t learn all those names and facts, much less
spell them correctly.
I mumbled something about trying harder, while Mr. Brunner took one
long sad look at the stele, like he’d been at this girl’s funeral.
He told me to go outside and eat my lunch.
The class gathered on the front steps of the museum, where we could watch
the foot traffic along Fifth Avenue.
Overhead, a huge storm was brewing, with clouds blacker than I’d ever
seen over the city. I figured maybe it was global warming or something,
because the weather all across New York state had been weird since
Christmas. We’d had massive snow storms, flooding, wildfires from
lightning strikes. I wouldn’t have been surprised if this was a hurricane
blowing in.
Nobody else seemed to notice. Some of the guys were pelting pigeons
with Lunchables crackers. Nancy Bobofit was trying to pickpocket something
from a lady’s purse, and, of course, Mrs. Dodds wasn’t seeing a thing.
Grover and I sat on the edge of the fountain, away from the others. We
thought that maybe if we did that, everybody wouldn’t know we were from
that school—the school for loser freaks who couldn’t make it elsewhere.
“Detention?” Grover asked.
“Nah,” I said. “Not from Brunner. I just wish he’d lay off me sometimes.
I mean—I’m not a genius.”
Grover didn’t say anything for a while. Then, when I thought he was
going to give me some deep philosophical comment to make me feel better,
he said, “Can I have your apple?”
I didn’t have much of an appetite, so I let him take it.
I watched the stream of cabs going down Fifth Avenue, and thought about
my mom’s apartment, only a little ways uptown from where we sat. I hadn’t
seen her since Christmas. I wanted so bad to jump in a taxi and head home.
She’d hug me and be glad to see me, but she’d be disappointed, too. She’d
send me right back to Yancy, remind me that I had to try harder, even if this
was my sixth school in six years and I was probably going to be kicked out
again. I wouldn’t be able to stand that sad look she’d give me.
Mr. Brunner parked his wheelchair at the base of the handicapped ramp.
He ate celery while he read a paperback novel. A red umbrella stuck up from
the back of his chair, making it look like a motorized café table.
I was about to unwrap my sandwich when Nancy Bobofit appeared in
front of me with her ugly friends—I guess she’d gotten tired of stealing from
the tourists—and dumped her half-eaten lunch in Grover’s lap.
“Oops.” She grinned at me with her crooked teeth. Her freckles were
orange, as if somebody had spray-painted her face with liquid Cheetos.
I tried to stay cool. The school counselor had told me a million times,
“Count to ten, get control of your temper.” But I was so mad my mind went
blank. A wave roared in my ears.
I don’t remember touching her, but the next thing I knew, Nancy was
sitting on her butt in the fountain, screaming, “Percy pushed me!”
Mrs. Dodds materialized next to us.
Some of the kids were whispering: “Did you see—”
“—the water—”
“—like it grabbed her—”
I didn’t know what they were talking about. All I knew was that I was in
trouble again.
As soon as Mrs. Dodds was sure poor little Nancy was okay, promising to
get her a new shirt at the museum gift shop, etc., etc., Mrs. Dodds turned on
me. There was a triumphant fire in her eyes, as if I’d done something she’d
been waiting for all semester. “Now, honey—”
“I know,” I grumbled. “A month erasing workbooks.”
That wasn’t the right thing to say.
“Come with me,” Mrs. Dodds said.
“Wait!” Grover yelped. “It was me. I pushed her.”
I stared at him, stunned. I couldn’t believe he was trying to cover for me.
Mrs. Dodds scared Grover to death.
She glared at him so hard his whiskery chin trembled.
“I don’t think so, Mr. Underwood,” she said.
“But—”
“You—will—stay—here.”
Grover looked at me desperately.
“It’s okay, man,” I told him. “Thanks for trying.”
“Honey,” Mrs. Dodds barked at me. “Now.”
Nancy Bobofit smirked. I gave her my deluxe I’ll-kill-you-later stare.
Then I turned to face Mrs. Dodds, but she wasn’t there. She was standing at
the museum entrance, way at the top of the steps, gesturing impatiently at me
to come on.
How’d she get there so fast?
I have moments like that a lot, when my brain falls asleep or something,
and the next thing I know I’ve missed something, as if a puzzle piece fell out
of the universe and left me staring at the blank place behind it. The school
counselor told me this was part of the ADHD, my brain misinterpreting
things.
I wasn’t so sure.
I went after Mrs. Dodds.
Halfway up the steps, I glanced back at Grover. He was looking pale,
cutting his eyes between me and Mr. Brunner, like he wanted Mr. Brunner to
notice what was going on, but Mr. Brunner was absorbed in his novel.
I looked back up. Mrs. Dodds had disappeared again. She was now inside
the building, at the end of the entrance hall.
Okay, I thought. She’s going to make me buy a new shirt for Nancy at the
gift shop.
But apparently that wasn’t the plan.
I followed her deeper into the museum. When I finally caught up to her,
we were back in the Greek and Roman section.
Except for us, the gallery was empty.
Mrs. Dodds stood with her arms crossed in front of a big marble frieze of
the Greek gods. She was making this weird noise in her throat, like growling.
Even without the noise, I would’ve been nervous. It’s weird being alone
with a teacher, especially Mrs. Dodds. Something about the way she looked
at the frieze, as if she wanted to pulverize it…
“You’ve been giving us problems, honey,” she said.
I did the safe thing. I said, “Yes, ma’am.”
She tugged on the cuffs of her leather jacket. “Did you really think you
would get away with it?”
The look in her eyes was beyond mad. It was evil.
She’s a teacher, I thought nervously. It’s not like she’s going to hurt me.
I said, “I’ll—I’ll try harder, ma’am.”
Thunder shook the building.
“We are not fools, Percy Jackson,” Mrs. Dodds said. “It was only a matter
of time before we found you out. Confess, and you will suffer less pain.”
I didn’t know what she was talking about.
All I could think of was that the teachers must’ve found the illegal stash
of candy I’d been selling out of my dorm room. Or maybe they’d realized I
got my essay on Tom Sawyer from the Internet without ever reading the book
and now they were going to take away my grade. Or worse, they were going
to make me read the book.
“Well?” she demanded.
“Ma’am, I don’t…”
“Your time is up,” she hissed.
Then the weirdest thing happened. Her eyes began to glow like barbecue
coals. Her fingers stretched, turning into talons. Her jacket melted into large,
leathery wings. She wasn’t human. She was a shriveled hag with bat wings
and claws and a mouth full of yellow fangs, and she was about to slice me to
ribbons.
Then things got even stranger.
Mr. Brunner, who’d been out in front of the museum a minute before,
wheeled his chair into the doorway of the gallery, holding a pen in his hand.
“What ho, Percy!” he shouted, and tossed the pen through the air.
Mrs. Dodds lunged at me.
With a yelp, I dodged and felt talons slash the air next to my ear. I
snatched the ballpoint pen out of the air, but when it hit my hand, it wasn’t a
pen anymore. It was a sword—Mr. Brunner’s bronze sword, which he always
used on tournament day.
Mrs. Dodds spun toward me with a murderous look in her eyes.
My knees were jelly. My hands were shaking so bad I almost dropped the
sword.
She snarled, “Die, honey!”
And she flew straight at me.
Absolute terror ran through my body. I did the only thing that came
naturally: I swung the sword.
The metal blade hit her shoulder and passed clean through her body as if
she were made of water. Hisss!
Mrs. Dodds was a sand castle in a power fan. She exploded into yellow
powder, vaporized on the spot, leaving nothing but the smell of sulfur and a
dying screech and a chill of evil in the air, as if those two glowing red eyes
were still watching me.
I was alone.
There was a ballpoint pen in my hand.
Mr. Brunner wasn’t there. Nobody was there but me.
My hands were still trembling. My lunch must’ve been contaminated with
magic mushrooms or something.
Had I imagined the whole thing?
I went back outside.
It had started to rain.
Grover was sitting by the fountain, a museum map tented over his head.
Nancy Bobofit was still standing there, soaked from her swim in the fountain,
grumbling to her ugly friends. When she saw me, she said, “I hope Mrs. Kerr
whipped your butt.”
I said, “Who?”
“Our teacher. Duh!”
I blinked. We had no teacher named Mrs. Kerr. I asked Nancy what she
was talking about.
She just rolled her eyes and turned away.
I asked Grover where Mrs. Dodds was.
He said, “Who?”
But he paused first, and he wouldn’t look at me, so I thought he was
messing with me.
“Not funny, man,” I told him. “This is serious.”
Thunder boomed overhead.
I saw Mr. Brunner sitting under his red umbrella, reading his book, as if
he’d never moved.
I went over to him.
He looked up, a little distracted. “Ah, that would be my pen. Please bring
your own writing utensil in the future, Mr. Jackson.”
I handed Mr. Brunner his pen. I hadn’t even realized I was still holding it.
“Sir,” I said, “where’s Mrs. Dodds?”
He stared at me blankly. “Who?”
“The other chaperone. Mrs. Dodds. The pre-algebra teacher.”
He frowned and sat forward, looking mildly concerned. “Percy, there is
no Mrs. Dodds on this trip. As far as I know, there has never been a Mrs.
Dodds at Yancy Academy. Are you feeling all right? 
"""
transitions = {}

"""
Build the Markov Chain

1. Split the text into words
2. Iterate over the words
3. For each word, add the next word to the list of transitions

TODO: Handle punctuation and capitalization for better results
"""
 
text = text.lower() # lowercase everything to make sure there aren't random capitalized letters/words
words = (re.findall(r'[\w]+|[^\s\w]', text)) # splits the text into words and punctuation
for i in range(len(words) - 1):
    current_word = words[i] # current_word is now either a word or puntuation
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)

"""
Generate new text using the Markov Chain, starting with a given word and
generating a specified number of words:

1. Start with the given word
2. Add the word to the result list
3. For the specified number of words:
    a. If the current word is in the transitions dictionary, choose a random next word
    b. Add the next word to the result list
    c. Update the current word to the next word
4. Return the generated text as a string

TODO: Clean up the generated text for better formatting and readability,
e.g., capitalization, punctuation, line breaks, etc.
"""

def generate_text(start_word, num_words):
    current_word = start_word
    result = [current_word.capitalize()] # start the sentence with a capital letter
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break
    generated_text = " ".join(result) # stores the entire text into a variable for editing
    cleaned_text = re.sub(r'\s+(?=[.,!?;:”])', '', generated_text) # removes spaces before the punctuation but not after
    cleaned_text = re.sub(r'\s*([\'’—-])\s*', r'\1', cleaned_text) # removes spaces before and after the puncuation
    cleaned_text = re.sub(r'([“"])\s+', r'\1', cleaned_text) # removes spaces after the punctuation but not before
    cleaned_text = re.sub(r'([.!?])\s*(\w)', lambda m: m.group(1) + ' ' + m.group(2).upper(), cleaned_text) # Capitalizes a letter after a punctuation mark
    return cleaned_text # returns the fully cleaned text to print

"""
Example usage, generating 10 words starting with "Mary"

TODO: Accept user input for the starting word and number of words to generate
"""

import sys
start = str(sys.argv[1]) # takes string argument 
length = int(sys.argv[2]) # takes int argument

print(generate_text(str(start.lower()), int(length))) # prints the generated text and takes a string argument and a int argument