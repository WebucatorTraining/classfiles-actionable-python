# https://levelup.gitconnected.com/deploy-simple-and-instant-online-quizzes-with-jupyter-notebook-tools-5e10f37da531
from IPython.display import display, HTML
from ipywidgets import widgets, Layout, Box, GridspecLayout


##Basic mcq

def create_multipleChoice_widget(question, options, correct_answer, hint):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False,
        indent = False,
        align = 'center',
    )
    
    question_out = widgets.Output(layout=Layout(width='auto'))
    
    with question_out:
        display(HTML(question))
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '<strong style="color:green">Correct!</strong>'
        else:
            s = '<strong style="color:red">Try again.</strong>'
        with feedback_out:
            feedback_out.clear_output()
            display(HTML(s))
        return
    
    check = widgets.Button(description="check")
    check.on_click(check_selection)
    
    hint_out = widgets.Output()
    
    def hint_selection(b):
        with hint_out:
            display(HTML(hint))
            
        with feedback_out:
            feedback_out.clear_output()
            display(HTML(hint))
    
    hintbutton = widgets.Button(description="hint")
    
    if hint:
        hintbutton.on_click(hint_selection)
    else:
        hintbutton.disabled = True
        hintbutton.description = 'No hint'
    
    return widgets.VBox([question_out, 
                         alternativ, 
                         widgets.HBox([hintbutton, check]), feedback_out], 
                        layout=Layout(display='flex',
                                     flex_flow='column',
                                     align_items='stretch',
                                     width='auto')) 

##basic text input quiz

def create_textinputquiz_widget(question, label, correct_answer, a2, hint): ##grid for option table
    #correct_answer = correct_answer ##float ##str   
    alternativ = widgets.Text(value = '',
                             placeholder = '',
                             description = '',
                             disabled = False, layout=(Layout(width = 'auto'))
                             )
##question description
    question_out = widgets.Output(layout=Layout(width='auto')) 
    with question_out:
        display(HTML(question))
##description before text widget    
    label_out = widgets.Output(layout=Layout(width='auto'))  
    with label_out:
        display(HTML(label))
##description after text widget e.g. units        
    a2_out = widgets.Output(layout=Layout(width='auto'))  
    with a2_out:
        display(HTML(a2))  
##
    feedback_out = widgets.Output()
    def check_selection(b):
        a = alternativ.value
        if a == correct_answer:
            s = '<strong style="color:green">Correct!</strong>'
        else:
            s = '<strong style="color:red">Try again.</strong>'
        with feedback_out:
            feedback_out.clear_output()
            display(HTML(s))
        return
    
    check = widgets.Button(description="check")
    check.on_click(check_selection)
##
    hint_out = widgets.Output()    
    def hint_selection(b):
        with hint_out:
            display(HTML(hint))        
        with feedback_out:
            feedback_out.clear_output()
            display(HTML(hint))
    
    hintbutton = widgets.Button(description="hint")
    
    if hint:
        hintbutton.on_click(hint_selection)
    else:
        hintbutton.disabled = True
        hintbutton.description = 'No hint'

    return widgets.VBox([question_out,
                         widgets.HBox([label_out, alternativ, a2_out]), 
                         widgets.HBox([hintbutton, check]), feedback_out], 
                        layout=Layout(display='flex',
                                     flex_flow='column',
                                     align_items='stretch',
                                     width='auto'))