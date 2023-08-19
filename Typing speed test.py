import time

def typing_speed_test():
    prompt = "The quick brown fox jumps over the lazy dog"
    print("Type the following:")
    print(prompt)
    
    input("Press Enter when you are ready...")
    
    start_time = time.time()
    typed_text = input("Start typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words = len(typed_text.split())
    
    wpm = (words / elapsed_time) * 60
    
    print("\nTime taken: {:.2f} seconds".format(elapsed_time))
    print("Words typed: {}".format(words))
    print("Typing speed: {:.2f} WPM".format(wpm))

typing_speed_test()
