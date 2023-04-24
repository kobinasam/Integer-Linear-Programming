import java.util.*;
import java.gurobi.*;
public class ILP {

    public static void main(String[] args){
        try {
            // first we create a new environment and model
            GRBEnv env = new GRBEnv();
            GRBModel model = new GRBModel(env);

            // create a thousand variables
            GRBVar[] x = model.addVars(1000, GRB.BINARY);

            GRBLinExpr obj = new GRBLinExpr();
            for (int i = 0; i < 1000; i++) {
                obj.addTerm(1.0, x[i]);
            }
            model.setObjective(obj, GRB.MINIMIZE);

            GRBLinExpr sumExpr = new GRBLinExpr();
            for (int i = 0; i < 1000; i++) {
                sumExpr.addTerm(1.0, x[i]);
            }
            model.addConstr(sumExpr, GRB.GREATER_EQUAL, 100.0, "sum");

            for (int i = 0; i < 1000; i++) {
                model.addConstr(x[i], GRB.LESS_EQUAL, 1.0, "x" + i);
            }

            // set threads without parallels optimization
            model.getEnv().set(GRB.IntParam.Threads, 1);

            // optimize without parallels optimization
            model.optimize();
            System.out.println("Optimal solution without parallels: " + model.get(GRB.DoubleAttr.ObjVal));

            // set threads for parallels optimization
            model.getEnv().set(GRB.IntParam.Threads, 4);

            // optimize with parallels optimization
            model.optimize();
            System.out.println("Optimal solution with parallels: " + model.get(GRB.DoubleAttr.ObjVal));

            model.dispose();
            env.dispose();

        } catch (GRBException e) {
            System.out.println("Error code: " + e.getErrorCode() + ". " + e.getMessage());
        }
    }
}
