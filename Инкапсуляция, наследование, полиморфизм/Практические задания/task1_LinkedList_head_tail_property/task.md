Преднамеренное или непреднамеренное изменение некоторых характеристик экземпляра может нарушить логику вашей реализации.

Поэтому, чтобы пользователь не мог их модифицировать, необходимо сделать их либо закрытым или только в режиме чтения.

1. Атрибуты `head` и `tail` сделать защищенными, 
   чтобы они были доступны только внутри класса и всем наследникам данного класса.
   
1. Атрибут `len` заменить на свойство только с возможностью чтения.
