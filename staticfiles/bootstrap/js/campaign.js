$(document).ready(function() {
    function toggleMinusFundDist() {
        var active_rows = $("table.fund-dist tr[class^='row']").length - $("table.fund-dist tr[class^='row']:hidden").length
        if ( active_rows <4) { 
            $('table.fund-dist i.icon-minus-sign').hide();
        } 
        else {
            $('table.fund-dist i.icon-minus-sign').show();
        };
    };
    function toggleMinusRewards() {
        var active_rows = $("table.rewards tr[class^='row']").length - $("table.rewards tr[class^='row']:hidden").length
        if ( active_rows <4) { 
            $('table.rewards i.icon-minus-sign').hide();
        } 
        else {
            $('table.rewards i.icon-minus-sign').show();
        };
    };
    function toggleMinusTeam() {
        var active_rows = $("table.team-member tr[class^='row']").length - $("table.team-member tr[class^='row']:hidden").length
        if ( active_rows <2) { 
            $('table.team-member i.icon-minus-sign').hide();
        } 
        else {
            $('table.team-member i.icon-minus-sign').show();
        };
    };
    $(document).on('focusout', "input[name^='fund-dist-a']", display_total_funds);

    function display_total_funds (){
        var sum=0;

        $("input[name^='fund-dist-amt']").each(function(){
            if ($.isNumeric($(this).val())) {
                sum += parseInt($(this).val(),10);
                if ($(this).is(":hidden"))
                    sum -= parseInt($(this).val(), 10);
            }
        });
        $("#total").html($("input#id_target_amount").val());
        $("#from-fund").html(sum);
        if (parseInt($("span#total").text()) < parseInt($("span#from-fund").text())) {
            $("span#errors").html("<strong>&nbsp;&nbsp;You have exceeded your target amount.</strong>");
        }
        else {
            $("span#errors").html("");
        };
    };
    toggleMinusFundDist();
    toggleMinusRewards();
    toggleMinusTeam();
    $(document).on('click', 'table.fund-dist i.icon-plus-sign', function() {
            var new_cols = $(this).parents("tr").clone();
            var suffix = $("table.fund-dist tr").length;
            new_cols.children()[0].children[0].name = "fund-dist-desc"+suffix;
            new_cols.children()[1].children[0].name = "fund-dist-amt"+suffix;
            new_cols.children()[0].children[0].value = "";
            new_cols.children()[1].children[0].value = "";
            $(new_cols).removeAttr("class");
            $(new_cols).addClass("row"+suffix);
            $(this).parents('tbody').append(new_cols);
            toggleMinusFundDist();
        });
    $(document).on('click', 'table.rewards i.icon-plus-sign', function() {
            var new_cols = $(this).parents("tr").clone();
            var suffix = $("table.rewards tr").length+1;
            new_cols.children()[0].children[0].name = "rewards"+suffix;
            new_cols.children()[0].children[0].value = "";
            $(new_cols).removeAttr("class");
            $(new_cols).addClass("row"+suffix);
            $(this).parents('tbody').append(new_cols);
            toggleMinusRewards();
        });
    $(document).on('click', 'table.team-member i.icon-plus-sign', function() {
            var new_cols = $(this).parents("tr").clone();
            var suffix = $("table.team-member tr").length;
            new_cols.children()[0].children[0].name = "name"+suffix;
            new_cols.children()[1].children[0].name = "role"+suffix;
            new_cols.children()[2].children[0].name = "short-bio"+suffix;
            new_cols.children()[3].children[0].name = "fb-url"+suffix;            
            new_cols.children()[0].children[0].value = "";
            new_cols.children()[1].children[0].value = "";
            new_cols.children()[2].children[0].value = "";
            new_cols.children()[3].children[0].value = "";            
            $(new_cols).removeAttr("class");
            $(new_cols).addClass("row"+suffix);
            $(this).parents('tbody').append(new_cols);
            toggleMinusTeam();
        });
    $(document).on('click', 'table.rewards i.icon-minus-sign', function() {
            $(this).parents("tr").hide();
            toggleMinusRewards();
        });
    $(document).on('click', 'table.fund-dist i.icon-minus-sign', function() {
            $(this).parents("tr").hide();    
            toggleMinusFundDist();
    });
    $(document).on('click', 'table.team-member i.icon-minus-sign', function() {
            $(this).parents("tr").hide();    
            toggleMinusTeam();
    });
});