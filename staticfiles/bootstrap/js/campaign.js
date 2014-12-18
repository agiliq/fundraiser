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
            new_cols.children()[2].children[0].name = "short-description"+suffix;
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
            $(this).parents("tr").remove();
            toggleMinusRewards();
        });
    $(document).on('click', 'table.fund-dist i.icon-minus-sign', function() {
            $(this).parents("tr").remove();    
            toggleMinusFundDist();
    });
    $(document).on('click', 'table.team-member i.icon-minus-sign', function() {
            $(this).parents("tr").remove();    
            toggleMinusTeam();
    });

    $(document).on('keydown', 'input[name^=fund-dist-amt]', function (e) {
            // Allow: backspace, delete, tab, escape, enter and .
            if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
                 // Allow: Ctrl+A
                (e.keyCode == 65 && e.ctrlKey === true) || 
                 // Allow: home, end, left, right, down, up
                (e.keyCode >= 35 && e.keyCode <= 40)) {
                     // let it happen, don't do anything
                     return;
            }
            // Ensure that it is a number and stop the keypress
            if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
                e.preventDefault();
            }
        });

});