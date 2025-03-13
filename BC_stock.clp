(deftemplate demanda 0 100
  ((baja (0 1) (20 1) (40 0))
  (media (20 0) (50 1) (80 0))
  (alta (60 0) (85 1) (100 1))))

(deftemplate stock 0 100
  ((bajo (0 1) (20 1) (40 0))
  (medio (20 0) (50 1) (80 0))
  (alto (60 0) (85 1) (100 1))))

(deftemplate reposicion 0 100
  ((muy_baja (0 1) (10 1) (20 0))
  (baja (10 0) (20 1) (40 0))
  (media (30 0) (50 1) (70 0))
  (alta (60 0) (70 1) (90 0))
  (muy_alta (80 0) (90 1) (100 1))))

(defrule regla1
  (demanda alta) (stock bajo)
  =>
  (assert (reposicion muy_alta)))

(defrule regla2
  (demanda alta) (stock medio)
  =>
  (assert (reposicion alta)))

(defrule regla3
  (demanda alta) (stock alto)
  =>
  (assert (reposicion media)))

(defrule regla4
  (demanda media) (stock bajo)
  =>
  (assert (reposicion alta)))

(defrule regla5
  (demanda media) (stock medio)
  =>
  (assert (reposicion media)))

(defrule regla6
  (demanda media) (stock alto)
  =>
  (assert (reposicion baja)))

(defrule regla7
  (demanda baja) (stock bajo)
  =>
  (assert (reposicion media)))

(defrule regla8
  (demanda baja) (stock medio)
  =>
  (assert (reposicion baja)))

(defrule regla9
  (demanda baja) (stock alto)
  =>
  (assert (reposicion muy_baja)))