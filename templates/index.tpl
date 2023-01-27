{# templates/index.tpl #}
<!DOCTYPE html>
<html>
<head>
    <style>
        .center {
            display: flex;
            justify-content: center;
        }
        .div-table {
            display: table;
            margin: 0 auto;
            width: auto;
        }
        .div-table-row {
            display: table-row;
            width: auto;
            clear: both;
        }
        .div-table-col {
            float: left; 
            display: table-column;         
            width: 200px;         
            background-color: #FFF;  
        }
        .div-table-col-yellow {
            float: left; 
            display: table-column;         
            width: 200px;         
            background-color: yellow;  
        }
        .div-table-col-red {
            float: left; 
            display: table-column;         
            width: 200px;         
            background-color: red;  
        }
        .div-table-col-green {
            float: left; 
            display: table-column;         
            width: 200px;         
            background-color: green;  
        }
    </style>
</head>
<body>

<div class="center">
    <h1>Tested TLS Certificates</h1>
</div>
<div class="center"><p>Date: {{ today_date }}</p></div>

<div class="div-table">
    <div class="div-table-row">
        <div class="div-table-col">Domain</div>
        <div class="div-table-col">Expiration Date</div>
        <div class="div-table-col">Status</div>
    </div>
    {% for domain in domain_data %}
    <div>
        <div class="div-table-col">{{ domain }}</div>
        <div class="div-table-col">{{ domain_data[domain]['expire'] }}</div>
        {% if 'EXPIRATION_NOTICE' in domain_data[domain]['message'] %}
        <div class="div-table-col-yellow">WARN</div>
        {% elif not domain_data[domain]['valid'] %}
        <div class="div-table-col-red">INVALID</div>
        {% else %}
        <div class="div-table-col-green">OK</div>
        {% endif %}
    </div>
    {% endfor %}
</div>

</body>
</html>