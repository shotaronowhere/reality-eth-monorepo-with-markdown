$('form#ask-question-form').submit( function() {
    var qtext = $(this).find('#question-text').val();
    var bounty = $(this).find('#bounty').val();
    var step_delay = $(this).find('#step_delay').val();
    var deadline = $(this).find('#q_deadline').val();

    var d = new Date();
    deadline = Math.floor(d.getTime()/1000) + deadline * 24 * 60 * 60;
    step_delay = step_delay * 24 * 60 * 60;

    console.log('submitting question with value', qtext);

    Arbitrator.deployed().then(function(arb) {
        RealityCheck.deployed().then(function(rc) {
            return rc.askQuestion(qtext, arb.address, step_delay, deadline, 1, {from: account}, {value: bounty});
        }).then(function (result) {
            console.log('question asked.');
            console.log('question', result);
        }).catch(function(e) {
          console.log(e);
        });
    }).catch(function(e) {
        console.log(e);
    });
    return false;
});