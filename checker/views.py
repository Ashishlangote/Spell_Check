from django.shortcuts import render
from django.views import View
import phunspell

class SpellCheckView(View):
    template_name = 'base.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        language = request.POST.get('language')
        input_text = request.POST.get('custom-textarea-content')
        radio_input = request.POST.get('optionsRadios')
        l = input_text.split(' ')
        suggestions_list = []
        corrected_text = input_text   
        pspell = phunspell.Phunspell(language)

        for i in l:
            if not i.isupper():
                if not pspell.lookup(i):
                    suggestions = [s for s in pspell.suggest(i)]
                    if suggestions:
                        suggestions_list.extend(suggestions)
                    if radio_input and radio_input in suggestions:
                        corrected_text = corrected_text.replace(i, radio_input)
        no_mistakes_message = "No spelling mistakes found." if not suggestions_list else ""
        context = {
            'corrected_text': corrected_text,
            'suggestions': suggestions_list,
            'input': input_text,
            'message':no_mistakes_message
        }
        return render(request, self.template_name, context)
