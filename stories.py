class Story:
    """Madlibs story.

    To  make a story, pass a code, a title, a list of prompts,
    and the text of the template.

        >>> s = Story(
        ...     "simple",
        ...     "A Simple Tale",
        ...     ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def __repr__(self):
        return f"<Story code='{self.code}' title='{self.title}' prompts={self.prompts} template='{self.template[:30] + '...'}'>"

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "omg",
    "An Excited Adventure",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)
story3 = Story(
    "date",
    "How to Date the Coolest Guy/Girl in School",
    [
        "plural_noun",
        "adverb",
        "verb",
        "article_of_clothing",
        "body part",
        "adjective3",
        "noun",
        "another_body_part",
        "plural_noun",
        "another_body_part2",
        "noun2",
        "verb_ending_in_ing",
        "adjective",
        "adjective2",
        "verb2"
    ],
    """ 
    
          It's simple. Turn the {plural_noun}. Make him/her want {adverb} 
        to date you. Make sure you're always dressed to {adjective}. Each and 
        every day, wear a/an {article_of_clothing} that you know shows off 
        your {noun2} to advantage and make your {verb} look like a million {noun}.
        
        Even if the two of you make meaningful contact, don't admit it. No hugs or 
        {verb_ending_in_ing}. Just shake his/her {another_body_part} firmly. And 
        remember, when he/she asks you out, even though a chill may run down your 
        {another_body_part2} and you can't stop your {verb2} from {adjective}, 
        just play it {adjective2}. Take a long pause before answering in a very 
        {adjective3} voice. I'll have to {plural_noun} it over.  


    """
)

story4 = Story(
    "pirate",
    "Talk Like a Pirate",
    [
        "noun",
        "adjective",
        "verb",
        "adverb",
        "noun2",
        "adjective2",
        "plural_noun",
        "part_of_the_body",
        "noun3",
        "noun4",
        "part_of_the_body2"
    ],
    """
    
          Ye can always pretend to be a bloodthirsty {noun},
        threatening everyone by waving yer sword in the air, 
        but until ye learn to {adjective}, like a pirate, 
        ye'll never be {adjective2}, accepted as an authentic {verb}.

        So here's what ye do: Cleverly work into yer daily conversations,
        pirate phrases such as "Ahoy there, {adverb}", "Avast, ye {noun2}", 
        and "Shiver me {adjective2}". Remember to drop all yer gs when ye say 
        such words as sailin', spittin', and fightin'. This will give ye a/an 
        {plural_noun}, start to being recognized as a swashbucklin'. Once ye 
        have the lingo down pat, it helps to wear a three-cornered {noun3},
        on yer head, stash a/an {part_of_the_body}, in yer pants, and keep 
        a/an {part_of_the_body2}, perched atop yer{noun4}. 
        
        Aye, now ye be a real pirate!
        
        
        """
)

# Make dict of {code:story, code:story, ...}
stories = {s.code: s for s in [story1, story2, story3, story4]}
