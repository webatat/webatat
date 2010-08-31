/*!
 * Ext JS Library 3.0+
 * Copyright(c) 2006-2009 Ext JS, LLC
 * licensing@extjs.com
 * http://www.extjs.com/license
 */
// Application instance for showing user-feedback messages.

Ext.BLANK_IMAGE_URL = '/static/js/ext/resources/images/default/s.gif';

var App = new Ext.App({});

// Create a standard HttpProxy instance.
var proxy = new Ext.data.HttpProxy({
    url: '/api/tasks'
});

// Typical JsonReader.  Notice additional meta-data params for defining the core attributes of your json-response
var reader = new Ext.data.JsonReader({
    totalProperty: 'total',
    successProperty: 'success',
    idProperty: 'id',
    messageProperty: 'message',
    root: 'data'
}, [
    {name: 'id'},
    {name: 'name', allowBlank: false},
    {name: 'complete', allowBlank: false}
]);

// The new DataWriter component.
var writer = new Ext.data.JsonWriter({
    encode: true,  //false // <-- don't return encoded JSON -- causes Ext.Ajax#request to send data using jsonData config rather than HTTP params
    writeAllFields: true
});

// Typical Store collecting the Proxy, Reader and Writer together.
var store = new Ext.data.Store({
    id: 'user',
    restful: true,     // <-- This Store is RESTful
    proxy: proxy,
    reader: reader,
    writer: writer,    // <-- plug a DataWriter into the store just as you would a Reader
    listeners: {
        write: function(store, action, result, response, rs) {
            App.setAlert(response.success, response.message);
        }
    }
});

// Let's pretend we rendered our grid-columns with meta-data from our ORM framework.
var userColumns =  [
    {header: "ID", width: 40, sortable: true, dataIndex: 'id'},
    {header: "Name", width: 100, sortable: true, dataIndex: 'name', editor: new Ext.form.TextField({})},
    {
        header: "Complete", 
        width: 50, 
        sortable: true, 
        dataIndex: 'complete', 
        editor: new Ext.form.Checkbox({}),
        renderer: function(value) {
            return "<input type='checkbox'" + (value ? "checked='checked'" : "") + ">";
        }    
    }
];

// load the store immeditately
store.load();

Ext.onReady(function() {
    Ext.QuickTips.init();

    // use RowEditor for editing
    var editor = new Ext.ux.grid.RowEditor({
        saveText: 'Update'
    });

    // Create a typical GridPanel with RowEditor plugin
    var userGrid = new Ext.grid.GridPanel({
        renderTo: 'user-grid',
        iconCls: 'icon-grid',
        frame: true,
        title: 'To-Do List',
        autoScroll: true,
        height: 300,
        store: store,
        plugins: [editor],
        columns : userColumns,
        tbar: [{
            text: 'Add',
            iconCls: 'silk-add',
            handler: onAdd
        }, '-', {
            text: 'Delete',
            iconCls: 'silk-delete',
            handler: onDelete
        }],
        viewConfig: {
            forceFit: true
        },
        listeners: {
            rowdblclick: function(grid, idx, e) {
                var sm = grid.getSelectionModel();
                if (sm.hasSelection) {
                    var record = sm.getSelected();
                }   
                form1.getForm().load({
                    url: '/api/tasks/' + record.id,
                    method: 'GET'
                });
                this.destroy();
                form1.render('user-grid');
            }
        }
        
    });

    function onAdd(btn, ev) {
        var u = new userGrid.store.recordType({
            name : '',
            complete: ''
        });
        editor.stopEditing();
        userGrid.store.insert(0, u);
        editor.startEditing(0);
    }

    function onDelete() {
        var rec = userGrid.getSelectionModel().getSelected();
        if (!rec) {
            return false;
        }
        userGrid.store.remove(rec);
    }
    
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
            text: 'Cancel',
            scope: this,
            handler: function() {
                form1.destroy();
                userGrid.render('user-grid');
            }               
        }]
    });
    
});
