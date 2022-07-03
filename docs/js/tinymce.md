
tinymce@6


https://www.tiny.cloud/docs/tinymce/6/

## vite 使用

```js title="editor.js"
import tinymce from 'tinymce'
import 'tinymce/icons/default'
import 'tinymce/themes/silver'
import 'tinymce/models/dom'

import 'tinymce/plugins/advlist'
import 'tinymce/plugins/anchor'
import 'tinymce/plugins/autolink'
import 'tinymce/plugins/autoresize'
import 'tinymce/plugins/autosave'
import 'tinymce/plugins/charmap'
import 'tinymce/plugins/code'
import 'tinymce/plugins/codesample'
import 'tinymce/plugins/directionality'
import 'tinymce/plugins/emoticons/js/emojis'
import 'tinymce/plugins/emoticons'
import 'tinymce/plugins/fullscreen'
import 'tinymce/plugins/help'
import 'tinymce/plugins/image'
import 'tinymce/plugins/importcss'
import 'tinymce/plugins/insertdatetime'
import 'tinymce/plugins/link'
import 'tinymce/plugins/lists'
import 'tinymce/plugins/media'
import 'tinymce/plugins/nonbreaking'
import 'tinymce/plugins/pagebreak'
import 'tinymce/plugins/preview'
import 'tinymce/plugins/quickbars'
import 'tinymce/plugins/save'
import 'tinymce/plugins/searchreplace'
import 'tinymce/plugins/table'
import 'tinymce/plugins/template'
import 'tinymce/plugins/visualblocks'
import 'tinymce/plugins/visualchars'
import 'tinymce/plugins/wordcount'

import 'tinymce/skins/ui/oxide/skin.css'
import skinContentCss from 'tinymce/skins/ui/oxide/content.css'
import contentCss from 'tinymce/skins/content/default/content.css'

tinymce.init({
    selector: '#textarea',
    min_height: window.innerHeight - 50,
    max_height: window.innerHeight - 50,
    plugins:
        'advlist anchor autolink autoresize autosave ' +
        'charmap code codesample directionality emoticons ' +
        'fullscreen help image importcss insertdatetime link lists media ' +
        'nonbreaking pagebreak preview quickbars save searchreplace ' +
        'table template visualblocks visualchars wordcount'
    ,
    skin: false,
    content_css: false,
    content_style: contentCss + skinContentCss,

    images_upload_handler: (blobInfo, progress) => new Promise((resolve, reject) => {
        const fileName = blobInfo.filename().split('.')[1] || "png"
        resolve(`data:image/${fileName};base64,${blobInfo.base64()}`)
    })

})

```
