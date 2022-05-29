from attr import field
from django import forms

from . import models


class CreateNewList(forms.Form):
    name=forms.CharField(label="Name",max_length=200)

class DeleteList(forms.Form):
    #i was trying to make this __init__ work but seems to be buggy
    def __init__(self,maxValue:int, *args, **kwargs):
        super(DeleteList, self).__init__(*args, **kwargs)
        self.fields['id'] = forms.IntegerField(label="Enter id",min_value=1,max_value=maxValue)
    id = forms.IntegerField()    
    
    #id=forms.IntegerField(label="Enter id",min_value=1,max_value=10) #-- only this seems to work
        #self.maxValue=maxValue
    #def __init__(self, data: Optional[_DataT] = ..., files: Optional[_FilesT] = ..., auto_id: Union[bool, str] = ..., prefix: Optional[str] = ..., initial: Optional[Mapping[str, Any]] = ..., error_class: Type[ErrorList] = ..., label_suffix: Optional[str] = ..., empty_permitted: bool = ..., field_order: Optional[Iterable[str]] = ..., use_required_attribute: Optional[bool] = ..., renderer: Optional[BaseRenderer] = ...) -> None:
    #    super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, field_order, use_required_attribute, renderer)
