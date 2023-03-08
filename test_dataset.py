issue_type_dataset = dataset ={
        'set_01': {
            'issue_type': 'Epic',
            'summary': 'Epic issue created by Selenium'}, # Should succeed to create issue
        
        'set_02': {
            'issue_type': 'Story',
            'summary': 'Story issue created by Selenium'}, # Should succeed to create issue
        
        'set_03': {
            'issue_type': 'Task',
            'summary': 'Task issue created by Selenium'}, # Should succeed to create issue
        
        'set_04': {
            'issue_type': 'Bug',
            'summary': 'Bug issue created by Selenium'}} # Should succeed to create issue

issue_summary_dataset = {
    'set_01': {'summary': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'}, # lowercase letters - Should succeed to create issue
    'set_02': {'summary': 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'}, # uppercase letters - Should succeed to create issue
    'set_03': {'summary': '1234567890'}, # numbers - Should succeed to create issue
    'set_04': {'summary': '!@#$%^&*()_+[]{};\':"|,./<>?'}, # special characters - Should succeed to create issue
    'set_05': {'summary': 'ąćęłóśźżĄĆĘŁÓŚŹŻ'}, # polish characters - Should succeed to create issue
    'set_06': {'summary': 'iwmvbzausqgoqcfwoauvhflrwwunhahhelisbrkvnnkrsofuuizyfqwcxenydgkbxpfchoudylhzhgpdfedqfxsnnponzxbnwaasxxajhgbrueownskkekaxooxxelxstgwclfgaoruusgizvcetntqcomqqfcdomunevrqolifssbfanznztfpxexcfrjkyiwjmjreeuqrzgrrzmsfbnzwemlubcqhawwfvywacopesfpoznjmchoxbljojzqb'}, # 255 characters = max length - Should succeed to create issue
    'set_07': {'summary': ''}, # empty string - Should fail to create issue
    'set_08': {'summary': '    '}, # only spaces - Should fail to create issue
    'set_09': {'summary': ' Test'}, # space at the beginning - Should succeed to create issue
    'set_10': {'summary': 'Test '}, # space at the end - Should succeed to create issue
    'set_11': {'summary': 'Test Spaces'}, # spaces in the middle - Should succeed to create issue
}

issue_label_dataset = {
    'set_01': {'labels': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                'summary': 'label lowercase alphabet'}, # lowercase letters - Should succeed to add label
    'set_02': {'labels': 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ',
                'summary': 'label uppercase alphabet'}, # uppercase letters - Should succeed to add label
    'set_03': {'labels': '1234567890',
                'summary': 'label numbers'}, # numbers - Should succeed to add label
    'set_04': {'labels': '!@#$%^&*()_+[]{};\':"|,./<>?',
                'summary': 'label special characters'}, # special characters - Should succeed to add label
    'set_05': {'labels': 'ąćęłóśźżĄĆĘŁÓŚŹŻ',
                'summary': 'label polish characters'}, # polish characters - Should succeed to add label
    'set_06': {'labels': 'iwmvbzausqgoqcfwoauvhflrwwunhahhelisbrkvnnkrsofuuizyfqwcxenydgkbxpfchoudylhzhgpdfedqfxsnnponzxbnwaasxxajhgbrueownskkekaxooxxelxstgwclfgaoruusgizvcetntqcomqqfcdomunevrqolifssbfanznztfpxexcfrjkyiwjmjreeuqrzgrrzmsfbnzwemlubcqhawwfvywacopesfpoznjmchoxbljojzqb',
                'summary': 'label character limit'}, # 255 characters = max length - Should succeed to create issue
    'set_07': {'labels': 'Q A',
                'summary': 'label contain spaces'} # space in the middle - Should fail to add label
}

issue_priority_dataset = {
    'set_01': {'priority': 'Lowest',
                'summary': 'priorityLowest'}, # Should succeed to change priority
    'set_02': {'priority': 'Low',
                'summary': 'priorityLow'}, # Should succeed to change priority
    'set_03': {'priority': 'Medium',
                'summary': 'priorityMedium'}, # Should succeed to change priority
    'set_04': {'priority': 'High',
                'summary': 'priorityHigh'}, # Should succeed to change priority
    'set_05': {'priority': 'Highest',
                'summary': 'priorityHighest'}, # Should succeed to change priority
}
