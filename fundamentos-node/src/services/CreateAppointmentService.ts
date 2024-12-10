// Responsável pela criação de agendamento

import Appointment from "../models/Appointments";
import AppointmentsRepository from '../repositories/AppointmentsRepository';
import { startOfHour } from "date-fns";


interface Request {
  provider: string;
  date: Date;
}

class CreateAppointmentService {
  private appointmentsRepository: AppointmentsRepository;
  constructor(appointmentsRepository: AppointmentsRepository) {
    this.appointmentsRepository = appointmentsRepository;
  }
  public execute({ provider, date }: Request): Appointment {
    const appoinmentDate = startOfHour(date);
    const findAppointmentInSameDate = this.appointmentsRepository.findByDate(appoinmentDate);

    if (findAppointmentInSameDate) {
      throw Error("This appoinment is already booked");
    }

    const appointment = this.appointmentsRepository.create({
      provider,
      date: appoinmentDate
    });
    return appointment;
  }
}

export default CreateAppointmentService;
