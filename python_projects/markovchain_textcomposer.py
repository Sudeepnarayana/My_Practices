import random
import re
from collections import defaultdict, Counter

class MarkovChainTextComposer:
    def __init__(self, n=2, punctuation=True, capitalization=True):
        """Initializes the Markov Chain text composer with added options."""
        self.n = n
        self.punctuation = punctuation  # Whether to include punctuation in the model
        self.capitalization = capitalization  # Preserve capitalization in generated text
        self.chain = defaultdict(Counter)  # Store word frequencies after n-grams
    
    def train(self, text):
        """Trains the Markov Chain with a given text."""
        # Tokenize the input text into words and punctuation (if necessary)
        if self.punctuation:
            # Regex includes punctuation marks separately
            words = re.findall(r'\b\w+\b|[.,!?;]', text.lower())
        else:
            # Only capture words
            words = re.findall(r'\b\w+\b', text.lower())
        
        # Create n-grams and populate the Markov chain dictionary with word frequencies
        for i in range(len(words) - self.n):
            key = tuple(words[i:i + self.n])  # n-gram key
            next_word = words[i + self.n]  # Next word after n-gram
            self.chain[key][next_word] += 1  # Increment frequency of next word
    
    def generate_text(self, length=100):
        """Generates random text based on the trained Markov Chain."""
        if not self.chain:
            return "Error: Markov Chain model is empty. Please train with a larger text corpus."
        
        # Start with a random n-gram from the chain keys
        current_state = random.choice(list(self.chain.keys()))
        output_words = list(current_state)
        
        for _ in range(length - self.n):
            # If the current state doesn't have any next word, break out of the loop
            if current_state not in self.chain:
                break
            
            # Choose the next word using weighted random choice
            next_word = self._weighted_random_choice(self.chain[current_state])
            output_words.append(next_word)
            
            # Update the current state to the new n-gram
            current_state = tuple(output_words[-self.n:])
        
        # If capitalization is enabled, capitalize the first word
        output_words = self._capitalize_text(output_words)
        
        # Join the words to form the final sentence
        return ' '.join(output_words)
    
    def predict_next_word(self, input_text):
        """Predicts the next word based on the user's input."""
        if not self.chain:
            return "Error: Markov Chain model is empty. Please train with a larger text corpus."
        
        # Tokenize the user input
        if self.punctuation:
            words = re.findall(r'\b\w+\b|[.,!?;]', input_text.lower())
        else:
            words = re.findall(r'\b\w+\b', input_text.lower())
        
        # Get the last n-gram from the user's input
        current_state = tuple(words[-self.n:])
        
        # If the n-gram exists in the chain, suggest the most likely next word
        if current_state in self.chain:
            next_word = self._weighted_random_choice(self.chain[current_state])
            return next_word
        
        return "No prediction available for the given input."
    
    def _weighted_random_choice(self, options):
        """Chooses a random word from the options, weighted by frequency."""
        total_weight = sum(options.values())  # Total frequency of all options
        rand_weight = random.randint(1, total_weight)  # Choose a random weight
        cumulative_weight = 0
        
        for word, weight in options.items():
            cumulative_weight += weight
            if cumulative_weight >= rand_weight:
                return word
        
        # Return the last word if something goes wrong (safety fallback)
        return random.choice(list(options.keys()))
    
    def _capitalize_text(self, words):
        """Capitalize the first word of the text or after punctuation."""
        if not words:
            return words
        
        # Capitalize the first word or after punctuation (.,!?)
        for i, word in enumerate(words):
            if i == 0 or words[i - 1] in [".", "!", "?"]:
                words[i] = word.capitalize()
            else:
                words[i] = word.lower()  # Ensure other words are lowercase
        return words

# Example usage
if __name__ == "__main__":
    # Sample text for training
    text = """
The forest hummed with life, a symphony of rustling leaves, chirping birds, and the distant babble of a brook winding its way through 
moss-covered rocks. A faint golden light filtered through the canopy, casting dappled patterns on the forest floor where mushrooms 
sprouted in clusters like tiny, otherworldly umbrellas. "This place feels alive," she murmured, her voice barely above a whisper, 
as if speaking louder might disturb the ancient spirits of the woods. The wind carried with it the scent of pine and earth, 
mingling with the faint aroma of wildflowers blooming somewhere nearby. In her mind, she replayed the instructions: walk straight
 until you see the old oak with the split trunk, then turn left. It sounded simple enough, yet every tree seemed to hold secrets, and 
 every path seemed eager to lead her astray. Somewhere above, a raven cawed, its echo fading into the vast, unending green. 
 She tightened her grip on her satchel, the faint weight of the parchment inside reminding her of the task ahead.
   "The answers lie beyond," the stranger had said, cryptic and calm, leaving her to decipher the meaning in her own way.
    """
    # Initialize the composer (e.g., bigram model)
    composer = MarkovChainTextComposer(n=2, punctuation=True, capitalization=True)

    # Train the model with the sample text
    composer.train(text)

    # Generate random text based on the model
    generated_text = composer.generate_text(length=50)
    print("Generated Text:")
    print(generated_text)
    
    # Predict the next word based on user input
    user_input =input("enter the word to predict the next one: ")
    prediction = composer.predict_next_word(user_input)
    print("\nUser Input:", user_input)
    print("Predicted Next Word:", prediction)
