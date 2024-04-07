from Backend.summaraize_app.video_generation import video_generator

def video_gen(summary):
    video_generator.video_gen_fun(summary)

summary = 'Your max_length is set to 100, but your input_length is only 9. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually'    
 
video_gen(summary)
