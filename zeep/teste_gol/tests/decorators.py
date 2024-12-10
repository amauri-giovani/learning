''' Decorators to print detailed endpoint return data such as availability and pricing
'''
import logging
import warnings


def _print_breakdown(breakdown):
    if not breakdown:
        return ""
    logq = '\n     Type Pax {}: {} (base) + {} (taxes) = {}'.format(
        breakdown['PaxType'],
        breakdown['Details']['base'],
        breakdown['Details']['taxes'],
        breakdown['Details']['total']
    )
    return logq


def log_availability(func):
    ''' This decorator log the availability
    '''
    
    def func_wrapper(self, *args, **kwargs):
                
        availability = func(self, *args, **kwargs)

        if hasattr(availability, 'error'):
            if availability.error:
                print("Errors: {}".format(availability.error))
                
        if not availability:
            print("!!!!!!!!!!!!!! No availability !!!!!!!!!!!!!!")
            return availability
                  
        itineraries = availability.itineraries
        
        if not itineraries:
            print("!!!!!!!!!!!!!! No itineraries !!!!!!!!!!!!!!")
            return availability

        log_avai = '*' * 15 + ' Availability ' + '*' * 15
        
        for itinerary in itineraries:
            log_avai += '\n\n' + ">>"*40
            log_avai += '\nItinerary: {}'.format(itinerary)
            for flight in itinerary.going_flights:
                log_avai += '\n> Flight: {}'.format(flight)
                for segment in flight.segments:
                    log_avai += '\n  *> {}'.format(segment)
                for fare in flight.fares:
                    log_avai += '\n > $ {}'.format(fare)
                    log_avai += _print_breakdown(fare.breakdown_adt)
                    log_avai += _print_breakdown(fare.breakdown_chd)
                    log_avai += _print_breakdown(fare.breakdown_inf)
                    log_avai += '\n\n'
            
        print(log_avai + '\n\n')
        
        return availability

    return func_wrapper


def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            warnings.simplefilter("ignore", FutureWarning)
            test_func(self, *args, **kwargs)
    return do_test
