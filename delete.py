def remove_used_fragment(file_path, fragment_to_remove):
    with open(file_path, 'r') as file:
        content = file.read()

    updated_content = content.replace(f'{fragment_to_remove}\n', '')
    
    try:
        with open(file_path, 'w') as file:
            file.write(updated_content)
        
        print(f"The fragment '{fragment_to_remove}' has been removed from the file.")
    
    except IOError:
        print(f"Error: Unable to write to file '{file_path}'.")

remove_used_fragment('outpu.txt','maxim_sudat')