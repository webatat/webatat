/*!
 * Ext JS Library 3.0+
 * Copyright(c) 2006-2009 Ext JS, LLC
 * licensing@extjs.com
 * http://www.extjs.com/license
 */
Ext.onReady(function(){

    Ext.QuickTips.init();
    Ext.form.Field.prototype.msgTarget = 'side';
    
    var form1 = new Ext.FormPanel({
        url:'/api/tasks',
        frame:true,
        title: 'Simple Form',
        width: 500,
        items :[
            {
                xtype: 'textfield',
                fieldLabel: 'Name',
                name: 'name',
                allowBlank:false,
                width: 200                
            },
            {
                xtype: 'textarea',
                fieldLabel: 'Description',
                name: 'description',
                width: 200
            },
            {
                xtype: 'checkbox',
                fieldLabel: 'Complete',
                name: 'complete'
            }
        ],
        buttons: [{
            text: 'Save',
            formBind: true,
            scope: this,
            handler: function() {
                console.log(form1.form);
                form1.form.submit({
                    url: '/api/tasks/1',
                    method: 'PUT',
                    success: function(form, action){
                        alert('yes');
                    }
                });
            }
        },
        {
            text: 'Cancel'
        }]
    });

    form1.getForm().load({
        url: '/api/tasks/1',
        method: 'GET'
    });


    form1.render(document.body);
});