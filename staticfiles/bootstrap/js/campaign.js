$(document).ready(function() {
    function toggleMinusFundDist() {
        var active_rows = $("table.fund-dist tr[class^='row']").length - $("table.fund-dist tr[class^='row']:hidden").length
        if ( active_rows <3) { 
            $('table.fund-dist i.icon-minus-sign').hide();
        } 
        else {
            $('table.fund-dist i.icon-minus-sign').show();
        };
    };
    function toggleMinusRewards() {
        var active_rows = $("table.rewards tr[class^='row']").length - $("table.rewards tr[class^='row']:hidden").length
        if ( active_rows <3) { 
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
        function highlightRequiredFields(error) { 
            $(".form-horizontal input[type=text]").each(function() {
            if(!$(this).val()) {
                error+=1
                $(this).attr("class", "required");
                $(this).parents("table").siblings("span").attr("id", "required-fields");
                $(this).siblings("span").attr("id", "required-fields");
            }
            else {
                $(this).parents("table").siblings("span").html("");
                $(this).parents("table").siblings("span").removeAttr("id");
                $(this).siblings("span").html("");   
                $(this).siblings("span").removeAttr("id");
                $(this).removeAttr("class");
            };
        });
        if ((parseInt($("input#id_target_amount").val(), 10) == 0.0) || ($("input#id_target_amount").val().trim() == "")) {
            error+=1;
            $("input#id_target_amount").attr("class", "required");
            $("input#id_target_amount").siblings("span").html("Target Amount can not be zero or blank");
        }
        else {
            $("input#id_target_amount").removeAttr("class");
            $("input#id_target_amount").siblings("span").html("");
        }       
        if ($("select option:selected").val() == "") {
            error+=1;
            alert("Category not selected");
            $(this).attr("class", "required");
        }
        if ($("textarea").val().trim() == "" ) {
            error+=1;
            $("textarea").attr("class", "required");
            $("textarea").siblings("span").attr("id", "required-fields");
        }
        else {
            $("textarea").removeAttr("class");
            $("textarea").siblings("span").removeAttr("id");
            $("textarea").siblings("span").html("");
        }
        return error;
        };

        $("form.form-horizontal").on("submit",function(event) {
            if (parseInt($("span#total").text()) != parseInt($("span#from-fund").text())) {
                $("span#errors").html("<strong>&nbsp;&nbsp;Target amount and funds Distribution does not match</strong>");
                event.preventDefault();
            }
            error = highlightRequiredFields(0);
            if (error == 0) {
                console.log("adios");
            }
            else {
                $("span#required-fields").each(function() { $(this).html("Fields are required");});
                event.preventDefault();
            }

        });

});