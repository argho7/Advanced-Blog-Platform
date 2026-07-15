# TinyMCE Configuration
TINYMCE_DEFAULT_CONFIG = {
    'height': 500,
    'width': '100%',
    'menubar': 'file edit view insert format tools table help',
    'plugins': '''
        advlist autolink lists link image charmap print preview anchor
        searchreplace visualblocks code fullscreen
        insertdatetime media table paste code help wordcount
        ''',
    'toolbar': '''
        undo redo | bold italic underline strikethrough | 
        forecolor backcolor | alignleft aligncenter alignright | 
        bullist numlist | link image media | 
        code fullscreen preview | help
        ''',
    'toolbar_mode': 'sliding',
    'contextmenu': 'link image table',
    # 'images_upload_handler': 'handle_image_upload',  # Custom handler
    'images_upload_url': '/upload/image/',  
    'images_upload_credentials': True, 
    'images_reuse_filename': False,
    'images_upload_base_path': '/media/blog/post/images/',
    'automatic_uploads': True,
    'file_picker_types': 'image',
    'relative_urls': False,
    'remove_script_host': False,
    'convert_urls': True,
    'browser_spellcheck': True,
    'paste_data_images': True,
    'autoresize_bottom_margin': 50,
    'autoresize_on_init': True,
}